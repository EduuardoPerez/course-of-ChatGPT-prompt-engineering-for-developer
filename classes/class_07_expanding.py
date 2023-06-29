from main import get_completion


def execute():
    print("Welcome to class 07: Expanding")
    print("------------------------------")

    # given the sentiment from the lesson on "inferring",
    # and the original customer message, customize the email
    sentiment = "negative"

    # ** Customize the automated reply to a customer email
    # review for a blender
    review = """
    So, they still had the 17 piece system on seasonal \
    sale for around $49 in the month of November, about \
    half off, but for some reason (call it price gouging) \
    around the second week of December the prices all went \
    up to about anywhere from between $70-$89 for the same \
    system. And the 11 piece system went up around $10 or \
    so in price also from the earlier sale price of $29. \
    So it looks okay, but if you look at the base, the part \
    where the blade locks into place doesn't look as good \
    as in previous editions from a few years ago, but I \
    plan to be very gentle with it (example, I crush \
    very hard items like beans, ice, rice, etc. in the \
    blender first then pulverize them in the serving size \
    I want in the blender then switch to the whipping \
    blade for a finer flour, and use the cross cutting blade \
    first when making smoothies, then use the flat blade \
    if I need them finer/less pulpy). Special tip when making \
    smoothies, finely cut and freeze the fruits and \
    vegetables (if using spinach-lightly stew soften the \
    spinach then freeze until ready for use-and if making \
    sorbet, use a small to medium sized food processor) \
    that you plan to use that way you can avoid adding so \
    much ice if at all-when making your smoothie. \
    After about a year, the motor was making a funny noise. \
    I called customer service but the warranty expired \
    already, so I had to buy another one. FYI: The overall \
    quality has gone done in these types of products, so \
    they are kind of counting on brand recognition and \
    consumer loyalty to maintain sales. Got it in about \
    two days.
    """

    prompt = f"""
    You are a customer service AI assistant.
    Your task is to send an email reply to a valued customer.
    Given the customer email delimited by ```, \
    Generate a reply to thank the customer for their review.
    If the sentiment is positive or neutral, thank them for \
    their review.
    If the sentiment is negative, apologize and suggest that \
    they can reach out to customer service.
    Make sure to use specific details from the review.
    Write in a concise and professional tone.
    Sign the email as `AI customer agent`.
    Customer review: ```{review}```
    Review sentiment: {sentiment}
    """
    response = get_completion(prompt)
    print(response)
    # response
    # Dear Valued Customer,
    #
    # Thank you for taking the time to share your review with us. We appreciate your feedback and apologize for any
    # inconvenience you may have experienced.
    #
    # We are sorry to hear about the price increase you noticed in December. We strive to provide competitive pricing
    # for our products, and we understand your frustration. If you have any further concerns regarding pricing or any
    # other issues, we encourage you to reach out to our customer service team. They will be more than happy to assist
    # you.
    #
    # We also appreciate your feedback regarding the base of the system. We continuously work to improve the quality of
    # our products, and your comments will be taken into consideration for future enhancements.
    #
    # We apologize for any inconvenience caused by the motor issue you encountered. Our customer service team is always
    # available to assist with any warranty-related concerns. We understand that the warranty had expired, but we would
    # still like to address this matter further. Please feel free to contact our customer service team, and they will do
    # their best to assist you.
    #
    # Thank you once again for your review. We value your feedback and appreciate your loyalty to our brand. If you have
    # any further questions or concerns, please do not hesitate to contact us.
    #
    # Best regards,
    #
    # AI customer agent

    # ** Remind the model to use details from the customer's email
    prompt = f"""
    You are a customer service AI assistant.
    Your task is to send an email reply to a valued customer.
    Given the customer email delimited by ```, \
    Generate a reply to thank the customer for their review.
    If the sentiment is positive or neutral, thank them for \
    their review.
    If the sentiment is negative, apologize and suggest that \
    they can reach out to customer service.
    Make sure to use specific details from the review.
    Write in a concise and professional tone.
    Sign the email as `AI customer agent`.
    Customer review: ```{review}```
    Review sentiment: {sentiment}
    """
    # The "temperature" parameter in a language model allows for controlling the level of randomness in the model's
    # responses, with a higher temperature resulting in more diverse outputs, while a temperature of zero ensures
    # predictability and a more reliable system, making it suitable for applications where a predictable response is
    # desired, while a higher temperature is recommended for creative use cases seeking a wider variety of outputs.
    response = get_completion(prompt, temperature=0.7)
    print(response)
    # response
    # Dear valued customer,
    #
    # Thank you for taking the time to share your review with us. We appreciate your feedback and apologize for any
    # inconvenience caused by the recent price changes.
    #
    # We understand your concern about the price increase in December compared to the seasonal sale in November. We
    # strive to offer competitive prices and provide value to our customers. We apologize if this was not reflected in
    # your recent purchase.
    #
    # Regarding the quality of the base and the motor issue you experienced, we apologize for any disappointment caused.
    # We continuously strive to improve our products, and your feedback is valuable to us. We recommend reaching out to
    # our customer service team for further assistance with any product-related concerns you may have.
    #
    # Again, we apologize for any inconvenience you may have faced. We appreciate your loyalty and would like to ensure
    # your satisfaction. Please feel free to contact our customer service team, who will be more than happy to assist
    # you.
    #
    # Thank you for choosing our brand, and we hope to have the opportunity to serve you better in the future.
    #
    # Best regards,
    # AI customer agent


if __name__ == "__main__":
    execute()
