from flask import Flask, render_template, request, redirect, flash, url_for
from src.seed import add_contact, get_contact_by_id, get_contacts, delete_contact
from src.__init__ import app


@app.route("/", methods=['GET', 'POST'], strict_slashes=False)
def index():
    return render_template("base.html")


@app.route("/contacts", methods=['GET', 'POST'], strict_slashes=False)
def contacts():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        new_contact = add_contact(first_name, last_name, phone, email)
        if new_contact:
            flash(
                f'Contact {new_contact.first_name} {new_contact.last_name} was created', 'info')
        else:
            flash('Something went wrong. Try again!', 'error')
    contacts_all = get_contacts()
    return render_template("pages/contacts/contacts.html", contacts=contacts_all)


@app.route("/contacts/detail", methods=['POST'], strict_slashes=False)
def detail():
    if request.method == 'POST':
        contact_id = request.form.get('id')
        contact = get_contact_by_id(contact_id)
        if contact:
            return render_template("pages/contacts/detailContact.html", contact=contact)
        else:
            flash('Contact ID does not exist', 'error')
    return redirect(url_for('contacts'))


@app.route("/contacts/delete/<contact_id>", methods=['POST'], strict_slashes=False)
def delete(contact_id):
    if request.method == 'POST':
        delete_contact(contact_id)
        flash('Contact was deleted', 'info')
    return redirect(url_for('contacts'))

