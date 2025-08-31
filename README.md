# IELTS Platform

A comprehensive platform for IELTS preparation and practice, built with modern web technologies.

## 🏗️ Architecture

This project follows a monorepo structure with separate frontend and backend applications:

- **Frontend**: Next.js 15 with React 19, TypeScript, and Tailwind CSS
- **Backend**: FastAPI with Python, PostgreSQL (with pgvector), Redis, and MinIO
- **Database**: PostgreSQL with vector search capabilities for AI-powered features
- **Storage**: MinIO for file storage (S3-compatible)
- **Queue**: Redis for background job processing

📖 **Detailed Architecture Documentation**: See [`docs/ielts_platform_architecture_en.pdf`](docs/ielts_platform_architecture_en.pdf) for comprehensive system design and technical specifications.

## 📁 Project Structure

```
ielts-platform/
├── apps/
│   ├── api/                 # FastAPI backend
│   │   ├── core/           # Core configuration
│   │   ├── models/         # Database models
│   │   ├── routers/        # API endpoints
│   │   ├── schemas/        # Pydantic schemas
│   │   └── migrations/     # Database migrations
│   └── web/                # Next.js frontend
│       ├── src/
│       │   └── app/        # App router pages
│       └── public/         # Static assets
├── infra/
│   └── docker/             # Docker configurations
├── docker-compose.dev.yml   # Development environment
└── Makefile                # Build and deployment commands
```

## 🚀 Quick Start

### Prerequisites

- Docker and Docker Compose
- Node.js 18+ and pnpm
- Python 3.11+

### Development Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ielts-platform
   ```

2. **Start the development environment**
   ```bash
   docker-compose -f docker-compose.dev.yml up -d
   ```

3. **Install frontend dependencies**
   ```bash
   cd apps/web
   pnpm install
   ```

4. **Install backend dependencies**
   ```bash
   cd apps/api
   pip install -r requirements.txt
   ```

5. **Run database migrations**
   ```bash
   cd apps/api
   alembic upgrade head
   ```

6. **Start the development servers**

   **Frontend (Next.js):**
   ```bash
   cd apps/web
   pnpm dev
   ```
   Access at: http://localhost:3000

   **Backend (FastAPI):**
   ```bash
   cd apps/api
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```
   Access at: http://localhost:8000
   API docs at: http://localhost:8000/docs

### Services

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **PostgreSQL**: localhost:5432
- **Redis**: localhost:6379
- **MinIO Console**: http://localhost:9001
- **MinIO API**: http://localhost:9000

## 🛠️ Development

### Frontend Development

```bash
cd apps/web

# Install dependencies
pnpm install

# Start development server
pnpm dev

# Build for production
pnpm build

# Start production server
pnpm start

# Run linting
pnpm lint
```

### Backend Development

```bash
cd apps/api

# Install dependencies
pip install -r requirements.txt

# Run migrations
alembic upgrade head

# Start development server
uvicorn main:app --reload

# Create new migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head
```

### Database Management

```bash
# Access PostgreSQL
docker exec -it ielts-platform-postgres-1 psql -U ielts -d ielts

# Reset database
docker-compose -f docker-compose.dev.yml down -v
docker-compose -f docker-compose.dev.yml up -d
```

## 🐳 Docker

### Development Environment

```bash
# Start all services
docker-compose -f docker-compose.dev.yml up -d

# View logs
docker-compose -f docker-compose.dev.yml logs -f

# Stop services
docker-compose -f docker-compose.dev.yml down

# Rebuild services
docker-compose -f docker-compose.dev.yml build --no-cache
```

### Production Build

```bash
# Build frontend
docker build -f infra/docker/Dockerfile.web -t ielts-web .

# Build backend
docker build -f infra/docker/Dockerfile.api -t ielts-api .
```

## 🔧 Configuration

### Environment Variables

Create `.env` files in respective app directories:

**Frontend (.env.local):**
```env
NEXT_PUBLIC_API_BASE=http://localhost:8000
```

**Backend (.env):**
```env
DATABASE_URL=postgresql+psycopg://ielts:ielts@localhost:5432/ielts
REDIS_URL=redis://localhost:6379/0
S3_ENDPOINT=http://localhost:9000
S3_ACCESS_KEY=minio
S3_SECRET_KEY=minio12345
S3_BUCKET=assets
```

## 📚 Features

- **Modern Tech Stack**: Built with Next.js 15, React 19, and FastAPI
- **Vector Search**: PostgreSQL with pgvector for AI-powered content search
- **File Storage**: MinIO integration for scalable file management
- **Background Jobs**: Redis-based job queue system
- **Type Safety**: Full TypeScript and Pydantic integration
- **Development Experience**: Hot reload, Docker development environment

## 📖 Documentation

- **Architecture Guide**: [`docs/ielts_platform_architecture_en.pdf`](docs/ielts_architecture_en.pdf) - Comprehensive system design and technical specifications
- **API Documentation**: Available at http://localhost:8000/docs when running the backend
- **Database Schema**: Check `apps/api/migrations/` for database structure and changes

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

[Add your license information here]

## 🆘 Support

For questions or issues, please [create an issue](link-to-issues) or contact the development team.
