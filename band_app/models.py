from django.db import models
   
# Define a class for band members
class BandMember(models.Model): 
    """A class to represent a band member.

    Attributes:
    name (str): The name of the band member.
    role (str): The role of the band member, such as singer, guitarist, drummer, etc.
    bio (str): A short biography of the band member.
    """
    # Define a field for the name of the band member
    name = models.CharField(max_length=100) 
    # Define a field for the role of the band member
    role = models.CharField(max_length=100) 
    # Define a field for the bio of the band member
    bio = models.TextField()

    # Define a method to return the name of the band member as a string
    def __str__(self):
        """Return the name of the band member as a string.

        Returns:
        str: The name of the band member.
        """
        return self.name
    
# Define a class for contact information
class ContactInfo(models.Model): 
    """A class to represent contact information.

    Attributes:
    email (str): The email address of the contact.
    phone (str): The phone number of the contact.
    address (str): The address of the contact.
    """
    # Define a field for the email address
    email = models.EmailField() 
    # Define a field for the phone number
    phone = models.CharField(max_length=20) 
    # Define a field for the address
    address = models.CharField(max_length=200)

    # Define a method to return the email address as a string
    def __str__(self):
        """Return the email address of the contact as a string.

        Returns:
        str: The email address of the contact.
        """
        return self.email
