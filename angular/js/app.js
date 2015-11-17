var app = angular.module('HomeApp', ['ngRoute']);

app.config(['$routeProvider', function($routeProvider) {
 $routeProvider
 .when('/Login', {
   controller: 'LoginController',
   templateUrl: 'views/Login.html'
 })
 .when('/outbox/:id', {
   controller: 'EmailController',
   templateUrl: 'views/email.html'
 })
 .when('/register', {
   controller: 'EmailController',
   templateUrl: 'views/register.html'
 })
 .when('/resetpassword', {
   controller: 'EmailController',
   templateUrl: 'views/resetpassword.html'
 })
 .otherwise({
   redirectTo: '/Home'
 });
}]);
