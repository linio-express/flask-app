from flask import Flask

def create_app(config_filename=None):
    application = Flask(__name__, instance_relative_config=True)
    application.config.from_pyfile(config_filename)
    register_blueprints(application)
    application.secret_key='linioexp'
    return application
    application.jinja_env.globals.update(formato_de_precio=formato_de_precio)

def register_blueprints(application):
    from app.controllers.welcome_controller import inicio_page
    from app.controllers.productos_controller import producto_page
    from app.controllers.productos_por_canastas_controller import producto_por_canasta_page
    from app.controllers.canastas_controller import canasta_page
    from app.controllers.pedidos_controller import pedido_page
    from app.controllers.usuarios.sessions_controller import session_page
    from app.controllers.usuarios.registrations_controller import registration_page
    from app.controllers.categorias_controller import categoria_page
    application.register_blueprint(inicio_page)
    application.register_blueprint(producto_page)
    application.register_blueprint(producto_por_canasta_page)
    application.register_blueprint(canasta_page)
    application.register_blueprint(pedido_page)
    application.register_blueprint(session_page)
    application.register_blueprint(registration_page)
    application.register_blueprint(categoria_page)

def formato_de_precio(precio: float):
    precion=precio//1000
    preciov = int(precio) % 1000
    decimal=str(round(precio%1,2))
    decimalu=decimal[1:]
    if decimal=='1.0':
        decimalu = '.99'
    if preciov==0:
        preciov='000'
    if precion==0:
        if len(decimalu) == 0:
            print(str(preciov) + '.00')
            return str(preciov) + '.00'
        elif len(decimalu) == 2:
            print(str(preciov) + decimalu + '0')
            return str(preciov) + decimalu + '0'
        else:
            print(str(preciov) + decimalu)
            return str(preciov) + decimalu

    else:
        if len(decimalu)==0:
            if len(str(preciov)) != 3:
                preciov = str(0) * (3 - len(str(preciov))) + str(preciov)
                print(str(int(precion))+' '+preciov + '.00')
                return str(int(precion)) + ' ' + preciov + '.00'
            else:
                print(str(int(precion)) + ' ' + str(preciov) + '.00')
                return str(int(precion)) + ' ' + str(preciov) + '.00'
        elif len(decimalu)==2:
            if len(str(preciov))!=3:
                preciov = str(0)*(3-len(str(preciov)))+str(preciov)
                print(str(int(precion)) + ' ' + preciov + decimalu + '0')
                return str(int(precion)) + ' ' + preciov + decimalu + '0'
            else:
                print(str(int(precion)) + ' ' + str(preciov) + decimalu +'0')
                return str(int(precion)) + ' ' + str(preciov) + decimalu +'0'
        else:
            if len(str(preciov))!=3:
                preciov = str(0)*(3-len(str(preciov)))+str(preciov)
                print(str(int(precion)) + ' ' + preciov + decimalu + decimalu)
                return str(int(precion)) + ' ' + preciov + decimalu + decimalu
            else:
                print(str(int(precion)) + ' ' + str(preciov) + decimalu)
                return str(int(precion)) + ' ' + str(preciov) + decimalu
