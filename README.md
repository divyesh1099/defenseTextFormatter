# Defense Text Formatter

Defense Text Formatter is a Django-based web application that leverages the power of AI to format plain text into structured, professional-looking software documentation. This tool is particularly useful for individuals and organizations looking to automate the formatting of their technical documents, ensuring a consistent and formal output suitable for official use.

## Features

- **AI-Driven Formatting**: Utilizes an AI model to identify and apply formatting to different sections of text such as titles, headings, lists, and code snippets.
- **Professional-Grade Documents**: Produces documents ready for professional use, with clear structure and readability.
- **User-Friendly Interface**: Offers a straightforward web interface for text input and formatting, minimizing the need for manual editing.

## Live Application

A live version of the application is hosted at [Defense Text Formatter Live](https://defenseformattertool.pythonanywhere.com/). Try it out to experience the ease of automated document formatting.

## Local Setup

To set up the project locally, follow these steps:

### Prerequisites

Ensure you have Python 3.8+ and pip installed on your system.

### Installation

Clone the repository to your local machine:

```sh
git clone https://github.com/divyesh1099/defenseTextFormatter.git
cd defenseTextFormatter
```

Create a virtual environment and activate it:

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the required dependencies:

```sh
pip install -r requirements.txt
```

Run migrations and start the Django development server:

```sh
python manage.py migrate
python manage.py runserver
```

Navigate to `http://127.0.0.1:8000/` in your web browser to use the application.

## Usage Instructions

1. Input the raw, unformatted text into the text box on the homepage.
2. Click the 'FORMAT TEXT' button to process your input.
3. The AI will analyze and return the formatted text in the preview area.
4. A download option will be available if you wish to obtain a `.docx` file of the formatted text.

## Deployment

This project is deployed on PythonAnywhere. To deploy your own instance, refer to the [PythonAnywhere documentation](https://help.pythonanywhere.com/pages/) for detailed instructions on setting up and configuring Django applications.

## Technologies Used

- **Django**: A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- **AI Model**: The backend uses an AI model for text analysis and formatting (specific model details can be included here).
- **PythonAnywhere**: A cloud-based hosting service that offers an easy avenue for deploying Python applications.

## Contributing

We welcome contributions to improve Defense Text Formatter. If you have suggestions or contributions, please open an issue or pull request in the repository.

## Authors

- **[Divyesh Nandlal Vishwakarma](https://github.com/divyesh1099)** - Creator and maintainer of the project.

## Acknowledgements

- Thanks to all the contributors who have invested time in improving this tool.
- Special thanks to the AI community for providing the resources needed for building this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.