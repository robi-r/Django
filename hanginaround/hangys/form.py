from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length= 100)
    email = forms.EmailField(max_length = 50)
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        print(f"Sending email from{self.cleaned_data['email']}"
              f"with message: {self.cleaned_data['message']}")