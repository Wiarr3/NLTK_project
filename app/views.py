from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Text
from .text_analyzer import process_whole
from . import db
from .text_analyzer import get_start_of_text

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        text = request.form.get('text')
        if len(text) > 0:
            newText = process_whole(raw_text=text, userId=current_user.id)
            db.session.add(newText)
            print(newText.user_id)
            print(newText.rawText)
            db.session.commit()
            flash('Text analyze successfully added to repository', category='success')
        else:
            flash('Empty input', category='error')
    return render_template('home.html', user=current_user)


@views.route('/history')
@login_required
def history():
    texts = Text.query.filter(Text.user_id == current_user.id).all()
    texts_to_table = [(i + 1, text.id, get_start_of_text(text.rawText)) for i, text in enumerate(texts)]

    return render_template('history.html', user=current_user, texts=texts_to_table)


@views.route('/record')
@login_required
def record():
    idd = request.args.get('id')
    text = Text.query.get(idd)
    headline = get_start_of_text(text.rawText)
    progress = text.sentiment * 100
    return render_template('record.html', user=current_user, text=text, headline=headline, progress = progress)


@views.route('/delete')
@login_required
def delete_text():
    idd = request.args.get('id')
    text = Text.query.get(idd)
    db.session.delete(text)
    db.session.commit()
    return redirect(url_for('views.history'))
