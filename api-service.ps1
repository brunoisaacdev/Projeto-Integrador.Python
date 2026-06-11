$ErrorActionPreference = "Continue"

$project = $PSScriptRoot
$logs = Join-Path $project "logs"
$logFile = Join-Path $logs "fastapi.log"

New-Item -ItemType Directory -Path $logs -Force | Out-Null
Set-Location $project

& .\.venv\Scripts\python.exe -m uvicorn app.main:app `
    --host 127.0.0.1 `
    --port 8000 *>> $logFile
