# DL3006: Do not use `latest` tag 
# FROM ubuntu:latest 
# Use a specific, supported Ubuntu LTS tag instead of `latest` (DL3006)
FROM ubuntu:20.04   
######    


# Create a non-root user early (DL3003)
RUN groupadd -r appuser \
    && useradd -r -g appuser appuser

##### DL3008: Pin versions in apt-get #############
# RUN apt-get update          
# RUN apt-get install -y curl git


# CORRECTED Combine package operations into one layer, pin versions, clean up cache (DL3008)
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    curl=7.68.0-1ubuntu2.18 \
    git=1:2.25.1-1ubuntu3 \
    && rm -rf /var/lib/apt/lists/*

##################################



########## DL3004: Use COPY instead of ADD  ########
# ADD . /app                  

# CORRECTED ===  Use COPY instead of ADD for straightforward file copies (DL3004)
WORKDIR /app
COPY . /app


##### Set correct ownership and drop permissions on source files (DL3003)
RUN chmod -R 777 /app  
#RUN chown -R appuser:appuser /app


######### DL3003: Use a non-root user and proper permissions
# USER root
# Switch to non-root user (DL3003)
USER appuser

############

############# DL3018: Pin versions in `docker pull`, docker does always pull from official repo
CMD ["bash"]







