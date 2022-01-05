
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
    url = "https://amhep.pythonanywhere.com/grades/" + fullName;
    xhttp.open("GET", url, true);
    xhttp.onload = function() {
      document.getElementById("demo").innerHTML = this.responseText;
    };
    xhttp.send();
  }
}

/* GET - displays all students and their grades */
function loadDoc2() {
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "https://amhep.pythonanywhere.com/grades", true);
  xhttp.onload = function() {
    document.getElementById("demo").innerHTML = this.responseText;
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
    xhttp.open("POST", "https://amhep.pythonanywhere.com/grades");
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.onload = function() {
      document.getElementById("demo").innerHTML = this.responseText;
    };
    const body = {"name": fullName, "grade": gradeValue};
    xhttp.send(JSON.stringify(body));
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
    url = "https://amhep.pythonanywhere.com/grades/"
    xhttp.open("PUT", url + fullName);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.onload = function() {
      document.getElementById("demo").innerHTML = this.responseText;
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
    xhttp.open("DELETE", "https://amhep.pythonanywhere.com/grades/" + fullName);
    xhttp.onload = function() {
      document.getElementById("demo").innerHTML = this.responseText;
    console.log(this.responseText)
    };
    xhttp.send();
  }
}