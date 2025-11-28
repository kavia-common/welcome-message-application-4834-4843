#!/bin/bash
cd /home/kavia/workspace/code-generation/welcome-message-application-4834-4843/welcome_backend
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi

