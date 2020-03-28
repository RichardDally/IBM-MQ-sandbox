###
### Compiled home made CPython 3 docker image upon Ubuntu.
###

FROM ubuntu:18.04

MAINTAINER r.dally@protonmail.com

RUN apt-get update -y

RUN apt-get install -y --no-install-recommends \
    bash \
    bc \
    ca-certificates \
    coreutils \
    debianutils \
    build-essential \
    file \
    findutils \
    gawk \
    grep \
    libc-bin \
    lsb-release \
    mount \
    passwd \
    procps \
    sed \
    tar \
    vim \
    wget

RUN apt-get install -y --no-install-recommends \
    zlib1g-dev \
    libncurses5-dev \
    libgdbm-dev \
    libnss3-dev \
    libssl-dev \
    libreadline-dev \
    libffi-dev

ARG PYTHON_MAJOR=3
ARG PYTHON_MINOR=8
ARG PYTHON_MICRO=2
ENV PYTHON_VERSION=${PYTHON_MAJOR}.${PYTHON_MINOR}.${PYTHON_MICRO}

RUN echo "Building CPython ${PYTHON_VERSION}"

ENV PYTHON_BINARY=python${PYTHON_MAJOR}.${PYTHON_MINOR}
ENV PYTHON_ARCHIVE_DIRECTORY=Python-${PYTHON_VERSION}
ENV PYTHON_ARCHIVE_FILENAME=${PYTHON_ARCHIVE_DIRECTORY}.tgz
ENV PYTHON_ARCHIVE_URL=https://www.python.org/ftp/python/${PYTHON_VERSION}/${PYTHON_ARCHIVE_FILENAME}
ENV ROOT_DIRECTORY=/tmp
ENV ARCHIVES_DIRECTORY=${ROOT_DIRECTORY}/PythonArchives
ENV EXTRACT_DIRECTORY=${ARCHIVES_DIRECTORY}/${PYTHON_ARCHIVE_DIRECTORY}

# Download archive
RUN mkdir --parents ${ARCHIVES_DIRECTORY}
RUN wget --quiet ${PYTHON_ARCHIVE_URL} --directory ${ARCHIVES_DIRECTORY}

# Extract archive
RUN tar --extract --file ${ARCHIVES_DIRECTORY}/${PYTHON_ARCHIVE_FILENAME} --directory ${ARCHIVES_DIRECTORY}

# Start compiling CPython
RUN cd ${EXTRACT_DIRECTORY} && ./configure --enable-optimizations
RUN cd ${EXTRACT_DIRECTORY} && make --jobs 8
RUN cd ${EXTRACT_DIRECTORY} && make altinstall

# Reset default python3 symbolic link
RUN unlink /usr/bin/python3
RUN ln -sv /usr/local/bin/${PYTHON_BINARY} /usr/bin/python3

# Remove shebang from /usr/bin/lsb_release to unblock pip (c.f. https://stackoverflow.com/q/44967202/5037799)
RUN sed -i 1d /usr/bin/lsb_release

# Update Python 3 essential modules
RUN python3 -m pip install -U pip setuptools
