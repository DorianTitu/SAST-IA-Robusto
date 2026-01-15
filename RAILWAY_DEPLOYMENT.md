# Railway Deployment Guide

## Quick Start

### 1. Connect Repository
1. Go to [railway.app](https://railway.app)
2. Click "New Project"
3. Select "Deploy from GitHub"
4. Authorize and select this repository

### 2. Configure Environment
No additional environment variables needed. The app will:
- Use PORT from Railway automatically
- Default to port 8000 if local

### 3. Deploy
Railway will automatically:
1. Detect the Dockerfile
2. Build the Docker image
3. Deploy to railway.app domain
4. Assign a public URL

## Configuration Files

- `Dockerfile` - Container build configuration
- `railway.json` - Railway-specific settings
- `.dockerignore` - Files to exclude from build

## How It Works on Railway

1. Railway reads `Dockerfile` from project root
2. Builds using `requirements.txt`
3. Installs Python dependencies
4. Copies application code
5. Starts with dynamic PORT environment variable
6. Exposes service on railway.app domain

## API Endpoints After Deployment

```
GET https://[your-railway-domain]/health
POST https://[your-railway-domain]/api/v1/analyze
POST https://[your-railway-domain]/api/v1/analyze-files
```

## Environment Variables

### Available
- `PORT` - Automatically set by Railway (default: 8000)
- `PYTHONUNBUFFERED` - Set to 1 for real-time logs

### Add Custom Variables
In Railway dashboard:
1. Go to Variables
2. Add any environment variables needed
3. Variables are injected at runtime

## Troubleshooting

### Build Fails
- Check `requirements.txt` dependencies
- Verify `Dockerfile` has correct paths
- Ensure `src/` directory structure is complete

### App Won't Start
- Check logs in Railway dashboard
- Verify PORT environment variable is used
- Confirm health endpoint responds

### Slow Build
- Review `.dockerignore` - too many files?
- Consider using Railway's cache
- Check internet speed for dependency downloads

## Scaling

### Increase Resources
In Railway dashboard:
1. Select your service
2. Go to Settings
3. Increase Gen CPU/Memory

### Multiple Instances
Not needed for this app, but available via Railway dashboard

## Monitoring

### View Logs
```
Railway Dashboard → Your Project → Logs
```

### Health Check
```
curl https://[your-railway-domain]/health
```

## Continuous Deployment

Every push to main branch will:
1. Trigger a build automatically
2. Test the build
3. Deploy if successful
4. Update the live URL

## First Deployment Checklist

- [ ] Repository connected to Railway
- [ ] Dockerfile in project root
- [ ] requirements.txt with dependencies
- [ ] src/ folder with complete structure
- [ ] No .env file with secrets
- [ ] PORT environment variable supported

Done! Your SAST app is now live on Railway.
