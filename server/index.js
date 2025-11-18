// Node backend server
// Express server entry file
const proApi = require("./api/proApi");
const bodyParser = require("body-parser");
const express = require("express");
const app = express();
const path = require("path");
const history = require("connect-history-api-fallback");

// Use permissive settings to allow cross-origin access
app.all("*", function(req, res, next) {
  // Set allowed cross-origin domain, * allows any domain
  res.header("Access-Control-Allow-Origin", "*");
  // Allowed header types
  res.header("Access-Control-Allow-Headers", "content-type");
  // Allowed cross-origin request methods
  res.header("Access-Control-Allow-Methods", "DELETE,PUT,POST,GET,OPTIONS");
  if (req.method.toLowerCase() == "options") res.send(200);
  // Let OPTIONS preflight request end quickly
  else next();
});

// Prevent blank page when using history mode for routing
app.use(history());

// Parse req.body parameters
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Backend API routes
app.use("/v2/api/property", proApi);

// Serve static files in production
app.use(express.static(path.join(__dirname, "../dist")));

// Listen on port
app.listen(8081,'127.0.0.1', () => {
  console.log("success listen at port: 8081");
});
