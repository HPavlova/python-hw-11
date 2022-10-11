from crypt import methods
from flask import Flask, render_template, request, redirect, session, flash
from . import app
from src.seed import (
                      add_contact,
                      get_contact_by_id,
                      get_contacts,
                      delete_contact)


@app.route("/", methods=['GET', 'POST'], strict_slashes=False)
def contacts():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        new_contact = add_contact(first_name, last_name, phone, email)
        flash(f'Contact {new_contact.first_name} {new_contact.last_name} was created')

    contacts = get_contacts()
    print(contacts)
    return render_template("templates/contacts.html", contacts=contacts)


@app.route("/detail/<contact_id>", methods=['POST'], strict_slashes=False)
def detail(contact_id):
    if request.method == 'POST':
        detail = get_contact_by_id(contact_id)
        return render_template("templates/detail.html", detail=detail)
    flash(f'Contact {contact_id} does not exist ')

@app.route("/delete/<contact_id>", methods=['POST'], strict_slashes=False)
def delete(contact_id):
    if request.method == 'POST':
        delete_contact(contact_id)
        flash('Contact was deleted')
        return redirect("/")
    return redirect("/")
