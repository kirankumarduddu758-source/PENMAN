# PenMan - Handwriting Learning Platform

A serverless backend API for a handwriting learning platform. Built with FastAPI and deployed on AWS Lambda, using DynamoDB for data persistence and SQS for asynchronous event processing.

## Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Serverless**: AWS Lambda
- **Database**: DynamoDB
- **Messaging**: SQS
- **Runtime**: Python 3.11
- **ASGI Adapter**: Mangum

---

## Installation & Setup

### Prerequisites

- Python 3.11+
- pip
- AWS CLI configured with appropriate credentials
- Git

### Local Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd backend
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - **Windows (PowerShell)**:
     ```bash
     .\venv\Scripts\Activate.ps1
     ```
   - **Windows (CMD)**:
     ```bash
     venv\Scripts\activate.bat
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure environment variables**
   - Create a `.env` file in the root directory (see [Environment Configuration](#environment-configuration))

---

## Project Structure

```
backend/
├── app/
│   ├── main.py                 # FastAPI app initialization & Lambda handler
│   ├── models.py               # Pydantic data models
│   ├── routes/
│   │   ├── registration.py     # User registration endpoints
│   │   ├── courses.py          # Courses listing endpoint
│   │   └── contact.py          # Contact form endpoint
│   └── services/
│       ├── dynamodb.py         # DynamoDB operations
│       └── sqs.py              # SQS message publishing
├── requirements.txt            # Python dependencies
├── template.yaml               # AWS SAM template for deployment
└── README.md                   # This file
```

---

## Running Locally

### Start the Development Server

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation

Interactive API docs are available at:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

---

## API Endpoints

### Health Check

- **Endpoint**: `GET /`
- **Description**: Health check endpoint
- **Response**:
  ```json
  {
    "status": "PenMan backend running"
  }
  ```

### Registration

- **Endpoint**: `POST /registration/`
- **Description**: Register a new user
- **Request Body**:
  ```json
  {
    "name": "string",
    "email": "string",
    "course": "string"
  }
  ```
- **Response**:
  ```json
  {
    "message": "Registration successful"
  }
  ```
- **Behavior**: Saves user data to DynamoDB and publishes a `NEW_REGISTRATION` event to SQS

### Courses

- **Endpoint**: `GET /courses/`
- **Description**: Retrieve available handwriting courses
- **Response**:
  ```json
  [
    {"name": "Cursive Writing", "duration": "4 Weeks"},
    {"name": "Italic Writing", "duration": "4 Weeks"},
    {"name": "Calligraphy Basics", "duration": "6 Weeks"}
  ]
  ```

### Contact

- **Endpoint**: `POST /contact/`
- **Description**: Submit a contact form message
- **Request Body**:
  ```json
  {
    "name": "string",
    "email": "string",
    "message": "string"
  }
  ```
- **Response**:
  ```json
  {
    "message": "Message received"
  }
  ```
- **Behavior**: Saves contact message to DynamoDB and publishes a `CONTACT_MESSAGE` event to SQS

---

## Environment Configuration

### Local Development

Create a `.env` file in the root directory:

```env
# AWS Configuration
AWS_REGION=us-east-1
TABLE_NAME=penman-data
QUEUE_URL=https://sqs.us-east-1.amazonaws.com/YOUR_ACCOUNT_ID/YOUR_QUEUE_NAME

# API Configuration
ENVIRONMENT=development
```

### AWS Lambda Deployment

Configure environment variables in `template.yaml`:

```yaml
Environment:
  Variables:
    TABLE_NAME: penman-data
    QUEUE_URL: YOUR_SQS_URL
    ENVIRONMENT: production
```

Or set via AWS Console/CLI:
```bash
aws lambda update-function-configuration \
  --function-name PenmanFunction \
  --environment Variables={TABLE_NAME=penman-data,QUEUE_URL=YOUR_SQS_URL}
```

### Required Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `AWS_REGION` | AWS region | `us-east-1` |
| `TABLE_NAME` | DynamoDB table name | `penman-data` |
| `QUEUE_URL` | SQS queue URL | `https://sqs.us-east-1.amazonaws.com/.../queue-name` |

---

## Deployment

### Deploy to AWS Using SAM

1. **Build the application**
   ```bash
   sam build
   ```

2. **Deploy**
   ```bash
   sam deploy --guided
   ```

3. **View deployment outputs**
   ```bash
   aws cloudformation describe-stacks --stack-name <stack-name>
   ```

---

## Contributing

We welcome contributions! Please follow these guidelines:

### Code Style

- Use [PEP 8](https://pep8.org/) style guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Format code with tools like `black` or `autopep8`

### How to Contribute

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Keep commits atomic and descriptive
   - Write clear commit messages

3. **Test your changes**
   ```bash
   # Run the app locally
   uvicorn app.main:app --reload
   
   # Test endpoints via Swagger UI or curl
   curl -X GET http://localhost:8000/docs
   ```

4. **Submit a pull request**
   - Describe what your PR does
   - Reference any related issues
   - Wait for review and address feedback

### Code Review Checklist

Before submitting a PR, ensure:
- [ ] Code follows PEP 8 style guidelines
- [ ] All new functions have docstrings
- [ ] Changes are tested locally
- [ ] No hardcoded credentials or sensitive data
- [ ] Commit messages are descriptive

---

## Troubleshooting

### Module Import Errors

```bash
# Ensure virtual environment is activated
# Activate venv and reinstall dependencies
pip install -r requirements.txt
```

### AWS Credentials Not Found

```bash
# Configure AWS CLI
aws configure

# Or set environment variables
set AWS_ACCESS_KEY_ID=your_key
set AWS_SECRET_ACCESS_KEY=your_secret
```

### DynamoDB Connection Issues

- Verify table exists and table name matches `TABLE_NAME` environment variable
- Ensure AWS credentials have DynamoDB permissions
- Check AWS region configuration

---

## License

[Add appropriate license information]

## Support

For issues and questions, please open an issue on the repository.
