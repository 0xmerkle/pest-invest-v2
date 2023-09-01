class Templates:

    template = """I hope this email finds you well. I wanted to reach out to introduce myself and express my interest in your company, [COMPANY NAME]. I have been following your work and I am impressed with the innovative solutions you provide.

    I would love to learn more about your company and explore potential collaboration opportunities. Please let me know if you would be available for a call or meeting to discuss further.

    Thank you for your time and consideration. I look forward to hearing from you.

    Best regards,
    [Your Name]"""

    @staticmethod
    def sign():
        with open('email_signature.txt', 'r') as f:
            signature = f.read()
            return signature
