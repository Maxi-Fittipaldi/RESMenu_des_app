from head import app
from itsdangerous import URLSafeTimedSerializer
import datetime
def generate_confirmation_token(mail)
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(mail, salt=app.config['SECURITY_PASSWORD_SALT'])

def confirm_token(token, expiration=3600)
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        mail = serializer.loads(
            token,
            salt=app.config['SECURITY_PASSWORD_SALT'],
            max_age=expiration
        )
    except:
        return False
    return mail
def confirm_mail()
    try
        mail =confirm_token(token)
    except
        flash('el codigo se encuentra expirado o es incorrecto', 'peligro')
        id = id.query.filter_by(mail=mail).first_or_404()
        if id.confirmed:
        flash('la cuenta a sido confirmada, por favor logearte', 'exito')
    else:
        id.confirmed = True
        id.confirmed_on = datetime.datetime.now()
        db.session.add(id)
        db.session.commit()
        flash('has verificado la cuenta, gracias', 'exito')
    return redirect(url_for(login.html))