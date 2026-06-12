FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV OMPI_ALLOW_RUN_AS_ROOT=1
ENV OMPI_ALLOW_RUN_AS_ROOT_CONFIRM=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends openmpi-bin libopenmpi-dev openssh-server build-essential \
    && pip install --no-cache-dir mpi4py \
    && mkdir -p /run/sshd \
    && sed -i 's/^#PermitRootLogin.*/PermitRootLogin yes/' /etc/ssh/sshd_config \
    && sed -i 's/^#PubkeyAuthentication.*/PubkeyAuthentication yes/' /etc/ssh/sshd_config \
    && sed -i 's/^#StrictModes.*/StrictModes no/' /etc/ssh/sshd_config \
    && apt-get purge -y --auto-remove build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/mpi
COPY integral_serial.py integral_mpi.py integral_mpi_nonblocking.py /opt/mpi/

CMD ["mpirun", "-n", "4", "python", "/opt/mpi/integral_mpi.py", "10000000"]
