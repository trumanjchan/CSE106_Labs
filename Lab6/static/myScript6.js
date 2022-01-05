
/* GET - displays the specified student's grade */
function loadDoc1() {
  var xhttp = new XMLHttpRequest();

  const fullName = prompt("Please enter a name (First Last)", "");
  console.log(fullName);
  if (fullName == "" || fullName == null) {
    document.getElementById("demo").innerHTML =
    "Please enter a name that is in the database!";
  }
  else {
    url = "http://127.0.0.1:5000/grades/" + fullName;
    xhttp.open("GET", url, true);
    xhttp.onload = function() {
      document.getElementById("demo").innerHTML = this.responseText;
      const x = JSON.parse(this.responseText)

      console.log(x)
      console.log("Logging: " + this.responseText)
    };
    xhttp.send();
  }
}

/* GET - displays all students and their grades */
function loadDoc2() {
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "http://127.0.0.1:5000/grades", true);
  xhttp.onload = function() {
    document.getElementById("demo").innerHTML = this.responseText;
    const x = JSON.parse(this.responseText)

    console.log(x)
    console.log("Logging: " + this.responseText)
  };
  xhttp.send();
}

/* POST - creates a new student name and grade | (will get error 409 conflict if entry already exists) */
function loadDoc3() {
  var xhttp = new XMLHttpRequest();

  const fullName = prompt("Please enter a name (First Last)", "");
  console.log(fullName);
  const gradeValue = prompt("Please enter their grade (float)", "");
  console.log(gradeValue);
  if (fullName == "" || fullName == null) {
    document.getElementById("demo").innerHTML =
    "Please enter a name that doesn't already exist!";
  }
  else {
    xhttp.open("POST", "http://127.0.0.1:5000/" + fullName + "/" + gradeValue);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.onload = function() {
      document.getElementById("demo").innerHTML = this.responseText;
      console.log("Logging: " + this.responseText)
    };
    const body = {"name": fullName, "grade": gradeValue};
    xhttp.send(JSON.stringify(body));
    console.log("Logging: " + body)
  }
}

/* PUT - edits the specified student's grade */
function loadDoc4() {
  var xhttp = new XMLHttpRequest();

  const fullName = prompt("Please enter a name (First Last)", "");
  console.log(fullName);
  const gradeValue = prompt("Please enter their grade (float)", "");
  console.log(gradeValue);
  if (fullName == "" || fullName == null) {
    document.getElementById("demo").innerHTML =
    "Please enter a name that is in the database to edit their grade!";
  }
  else {
    url = "http://127.0.0.1:5000/" + fullName + "/" + gradeValue;
    xhttp.open("PUT", url);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.onload = function() {
      document.getElementById("demo").innerHTML = this.responseText;
      console.log("Logging: " + this.responseText)
    };
    const body =  {"grade": gradeValue}
    xhttp.send(JSON.stringify(body));
  }
}

/* DELETE - removes a grade (entry) */
function loadDoc5() {
  var xhttp = new XMLHttpRequest();

  const fullName = prompt("Please enter a name (First Last)", "");
  console.log(fullName);
  if (fullName == "" || fullName == null) {
    document.getElementById("demo").innerHTML =
    "Please enter a name that is in the database to delete the entry!";
  }
  else {
    xhttp.open("DELETE", "http://127.0.0.1:5000/" + fullName);
    xhttp.onload = function() {
      document.getElementById("demo").innerHTML = this.responseText;
      console.log("Logging: " + this.responseText)
    };
    xhttp.send();
  }
}