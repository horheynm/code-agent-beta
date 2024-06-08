#!/bin/bash
#  CHECK GITHUB CREDENTIALS ARE VALID

# Check username and token 

load_env() {
  if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
  else
    echo ".env file not found!"
    exit 1
  fi
}

check_github_token() {
  local username=$1
  local token=$2
  response=$(curl -s -u "$username:$token" https://api.github.com/user)

  if echo "$response" | grep -q '"login":'; then
    echo "The GitHub token is valid."
    return 0
  else
    echo "The GitHub token is invalid."
    return 1
  fi
}

load_env
check_github_token "$GITHUB_USERNAME" "$GITHUB_TOKEN"
