var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "testForm"
});
const mysqli_query = function(qry){
con.connect(function(err) {
    if (err) throw err;
    con.query(qry, function (err, result, fields) {
      if (err) throw err;
      console.log(result);
    });
  });
}
module.exports = { mysqli_query };