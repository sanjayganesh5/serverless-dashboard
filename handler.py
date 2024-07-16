def hello(event, context):
    """
    AWS Lambda function handler.

    :param event: The event data passed to the Lambda function.
    :param context: The runtime information of the Lambda function.
    :return: A dictionary with the status code and a message.
    """
    # Print the event and context information (for debugging)
    print("Received event:", event)
    print("Received context:", context)

    # Process the event (this example simply echoes the event)
    response = {
        "statusCode": 200,
        "body": "Hello, world!",
        "event": event  # Echoing the event for demonstration
    }

    # Return the response
    return response
