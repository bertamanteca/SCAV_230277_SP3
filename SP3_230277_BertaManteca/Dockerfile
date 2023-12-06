# Use an official FFMPEG base image
FROM jrottenberg/ffmpeg:latest

# Set the working directory
WORKDIR /app

# Copy your image processing script (e.g., process_image.sh) into the container
COPY process_image.sh .

# Set the script as executable during the build process
RUN chmod +x process_image.sh

# Set the script as the entrypoint
ENTRYPOINT ["./process_image.sh"]



