# Use an official node runtime as a parent image
FROM node:latest

# Set the working directory
WORKDIR /usr/src/app

# Copy the setup script
COPY script.sh .

# Make the script script executable
RUN chmod +x script.sh

# Run the script script to create the React app and components
RUN ./script.sh

# Move into the created React app directory
WORKDIR /usr/src/app/project1

# Expose the port the app runs on
EXPOSE 3000

# Command to run the app
CMD ["npm", "start"]

