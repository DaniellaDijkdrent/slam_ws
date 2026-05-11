FROM duckietown/dt-core:ente

WORKDIR /code

COPY ./packages /code/packages
COPY ./launchers /launchers

CMD ["/launchers/default.sh"]