from behave import given, when, then #pylint: disable=E0611

def sleep():
	import time
	time.sleep(3)


@given('I am on my contact page')
def go_to_contact_page(context):
	br = context.browser
	br.get(context.base_url + '/contact/')

@when('I send a filled contact form')
def fill_contact_form_and_send(context):
	br = context.browser
	br.find_element_by_id('id_text').send_keys('hello world')
	br.find_element_by_id('id_name').send_keys('dastan')
	br.find_element_by_id('id_email').send_keys('alymbekovdastan1@gmail.com')
	br.find_element_by_id('submitBtn').click()

@then("I see a success message")
def see_success_message(context):
	br = context.browser
	assert br.find_element_by_id('success').text == "Ваше сообщение успешно отправлено. Спасибо!"
