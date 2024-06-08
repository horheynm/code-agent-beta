#!/bin/bash

# check OPENAI_API_KEY exists and is valid in .env


load_env() {
  if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
  else
    echo ".env file not found!"
    exit 1
  fi
}


check_openai_api_key() {
  local api_key=$1
  response=$(curl -s -H "Authorization: Bearer $api_key" https://api.openai.com/v1/models)

  if echo "$response" | grep -q '"id":'; then
    echo "The OpenAI API key is valid."
    return 0
  else
    echo "The OpenAI API key is invalid."
    return 1
  fi
}

load_env
check_openai_api_key "$OPENAI_API_KEY"
