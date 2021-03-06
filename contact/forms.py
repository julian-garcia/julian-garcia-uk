from django import forms

class ContactForm(forms.Form):
    email_address = forms.EmailField(label="Email Address",
                                     widget=forms.TextInput(attrs={'class': 'contact-form-input input paragraph-text',
                                                                   'placeholder': 'Email Address'}))
    message = forms.CharField(label="Your Message",
                              widget=forms.Textarea(attrs={'class': 'contact-form-input textarea input paragraph-text',
                                                           'placeholder': 'Your Message'}))
