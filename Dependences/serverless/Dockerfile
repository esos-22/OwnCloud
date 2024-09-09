FROM public.ecr.aws/lambda/python:3.11.2024.09.06.09

COPY requirements.txt ${LAMBDA_TASK_ROOT}

RUN pip install -r requirements.txt

COPY lambda_func.py ${LAMBDA_TASK_ROOT}

CMD [ "lambda_func.handler" ]
