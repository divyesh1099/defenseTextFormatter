import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import google.generativeai as genai  # Ensure you have a real library
from googleApiKey import googleApiKey  # Ensure your API key is properly stored and imported
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
import re

# Configure the generative AI model
genai.configure(api_key=googleApiKey)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat()

def generate_document_via_chat(raw_text):
    """
    This function constructs a detailed prompt for the AI to format the text
    according to specific rules and sends it through the chat interface.
    """
    instructions = '''
        Please format the following text into a structured document. Follow these specific formatting rules:

1. Titles: Identify any line that ends with a colon ':' as a title. Titles should be bold, uppercase, and underlined.

2. Subtopics: Subtopics are lines immediately following a title, without a trailing colon. Format subtopics with only the first letter of each word capitalized, bold, and underlined, followed by a dot.

3. Nesting Levels: Organize the content into a nested list with the following pattern:
   - First level: Use numeric ordering (1, 2, 3, ...).
   - Second level: Use lowercase alphabetic ordering (a, b, c, ...).
   - Third level: Use Roman numerals (i, ii, iii, ...).

4. Content under each title or subtopic should be listed as bullet points under the respective heading.

5. System Requirements and similar sections should be presented as nested bullet points without a leading title or subtopic.

6. Use indentation to denote different nesting levels clearly. Indent subtopics and their content further than their parent titles.

7. In bullet points, if there is a term followed by a description, format the term in bold and the description in regular text.

8. For any action items listed under a process or operation, use a hanging indent format where the action is bolded, and the explanation is on the same line, indented.

9. Error Handling and Troubleshooting sections should list issues and resolutions in a two-column table format with 'Issue' and 'Resolution' as headers.

10. Ensure that all formatting complies with the latest version of the Markdown syntax, which will be used for preview and downloading purposes.

Please provide the output in JSON format, where each section is a key, and the content, including styling tags, is provided as HTML strings. This format will be used for previewing in a web application and for generating downloadable documents.
        
    '''
    # Combine instructions with the raw text
    full_message = f"{instructions}\n\n{raw_text}"
    
    # Send the combined message to the AI chat model
    response = chat.send_message(full_message)
    
    # Assume response.text contains the AI-formatted text
    formatted_text = response.text if hasattr(response, 'text') else "Formatting failed."

    # Strip markdown code block tokens if present
    formatted_text = formatted_text.strip('```json').strip('```').strip()

    return formatted_text
    # return "This is a test response without calling the external API."

@csrf_exempt
def index(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            raw_text = data.get('text', '')
            formatted_text = generate_document_via_chat(raw_text)
            
            # Send a JsonResponse with formatted_text which is already a JSON string
            return JsonResponse({'formatted_text': formatted_text})
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    # If it's not a POST request, just render the page without context
    return render(request, 'home/index.html')



@csrf_exempt
@require_http_methods(["POST"])
def send_message(request):
    try:
        # Extract the message from request
        data = json.loads(request.body)
        message = data['message']

        # Send message to the chat model and get response
        response = chat.send_message(message)

        # Return the chatbot's response
        return JsonResponse({'response': response.text})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

def create_docx_from_json(json_data, file_path):
    document = Document()

    def add_title(title):
        p = document.add_paragraph()
        run = p.add_run(title.upper())
        run.bold = True
        run.underline = True
        font = run.font
        font.size = Pt(14)
        p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

    def add_subtopic(subtopic):
        p = document.add_paragraph()
        run = p.add_run(subtopic.capitalize() + '.')
        run.bold = True
        run.underline = True
        font = run.font
        font.size = Pt(12)

    def add_content(content, level=0):
        if isinstance(content, dict):
            for k, v in content.items():
                if k.endswith(':'):
                    add_title(k[:-1])
                else:
                    add_subtopic(k)
                add_content(v, level + 1)
        elif isinstance(content, list):
            for item in content:
                document.add_paragraph(item, style='ListBullet')
        else:
            document.add_paragraph(content)

    add_content(json_data)

    document.save(file_path)