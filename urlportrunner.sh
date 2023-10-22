#!/bin/bash

# Define the URL and Port Range
url="http://example.com"
port_range="80 443"

# Function to get a random user agent
get_random_user_agent() {
    user_agent=$(python -c "from fake_useragent import UserAgent; print(UserAgent().random)")
    echo "$user_agent"
}

for port in $port_range; do
    user_agent=$(get_random_user_agent)
    response=$(curl -sI -A "$user_agent" "${url}:${port}")
    
    # Check for images, videos, or content length > 26
    if echo "$response" | grep -qE "Content-Type: (image|video)" || [ $(echo "$response" | grep -i "Content-Length" | cut -d ' ' -f 2) -gt 26 ]; then
        echo "Valid response on port $port"
        exit 0  # Exit with success status code
    fi
done

echo "No response"
exit 1  # Exit with failure status code



#Write me a shell script.
#The script should enumerate only the port number and should there be any image or video or content length more than 26,
#return a valid response, else display as no response