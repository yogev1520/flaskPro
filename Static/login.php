<html>
<body>
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
<form action="login.php" method="POST">
Name: <input type="usr" name="name"><br>
E-mail: <input type="email" name="email"><br>
E-mail: <input type="pwd" name="password"><br>
<input type="submit">
</form>

<div class="container">
    <h2>Form control: input</h2>
    <p>The form below contains two input elements; one of type text and one of type password:</p>
    <form action="/static/login.php">
        
        <div class="form-group">
        <label for="usr">Name:</label>
        <input type="text" id="usr" name="username">
        </div>

        <div class="form-group">
        <label for="pwd">Password:</label>
        <input type="password" id="pwd" name="password">
        </div>

        <div class ="form-group">
        <label for="email">email</label>
        <input type="email" id="email" name="email">
        </div>

        <button type="submit" class="btn_submit">Submit</button>
        
    </form>
</div>
</body>
</html>

