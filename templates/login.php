<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="{{ url_for('static', filename='css/login.css') }}">
    <link rel="icon" href="{{url_for('static', filename='img/icono_2-removebg-preview.ico')}}">
    <link rel="stylesheet" href="https://kit.fontawesome.com/64d58efce2.js" crossorigin="anonymous">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
    <script src="https://kit.fontawesome.com/64d58efce2.js" crossorigin="anonymous"></script>
    <title>Wirds Inc.</title>
  </head>
  <body>
    <div class="container">
      <div class="forms-container">
        <div class="signin-signup">
          <form action="/login" method="POST" class="sign-in-form">
            <img src="{{url_for('static', filename='img/WIRDS__positivo2_-removebg.png')}}" alt="">
            {% if error_message %}
            <div class="error-message">
                <i class="fas fa-exclamation-circle"></i>
                <span>{{ error_message }}</span>
            </div>
            {% endif %}
            <div class="input-field">
                <i class="fas fa-user"></i>
                <input type="text" name="username" placeholder="Usuario" required />
            </div>
            <div class="input-field">
                <i class="fas fa-lock"></i>
                <input type="password" name="password" placeholder="Contraseña" required />
            </div>
            <input type="submit" value="Iniciar Sesión" class="btn solid" />
          </form>
        
          <form action="#" class="sign-up-form">
            <img src="{{url_for('static', filename='img/WIRDS__positivo2_-removebg.png')}}" alt="">
            <div class="input-field">
              <i class="fas fa-signature"></i>
              <input type="text" placeholder="Nombres" />
            </div>
            <div class="input-field">
              <i class="fas fa-user"></i>
              <input type="text" placeholder="Usuario" />
            </div>
            <div class="input-field">
              <i class="fas fa-envelope"></i>
              <input type="email" placeholder="Correo" />
            </div>
            <div class="input-field">
              <i class="fas fa-lock"></i>
              <input type="password" placeholder="Contraseña" />
            </div>
            <input type="submit" class="btn" value="Registrarse" />
          </form>
        </div>
      </div>

      <div class="panels-container">
        <div class="panel left-panel">
          <div class="content">
            <h3>Nuevo Aqui?</h3>
            <p>
              Wirds Inc. Keep Track
            </p>
            <button class="btn transparent" id="sign-up-btn">
              Registrarse
            </button>
          </div>
          <img src="{{url_for('static', filename='img/undraw_team_page_re_cffb.svg')}}" class="image" alt="" />
        </div>
        <div class="panel right-panel">
          <div class="content">
            <h3>Tienes Cuenta?</h3>
            <p>
              Wirds Inc. Keep Track 
            </p>
            <button class="btn transparent" id="sign-in-btn">
              Iniciar Sesion
            </button>
          </div>
          <img src="{{url_for('static', filename='img/undraw_pay_online_re_aqe6.svg')}}" class="image" alt="" />
        </div>
      </div>
    </div>

    <script src="{{url_for('static', filename='js/login.js')}}"></script>
    <script>
      setTimeout(function() {
        var errorDiv = document.querySelector(".error-message");
        if (errorDiv) {
          errorDiv.style.display = "none";
        }
      }, 2000); // Ocultar el mensaje de error después de 2000 ms (2 segundos)
    </script>
    
  </body>
</html>