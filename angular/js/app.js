var app = angular.module('HomeApp', ['ngRoute']);

app.config(['$routeProvider', function($routeProvider) {
 $routeProvider
 .when('/Register', {
   controller: 'RegisterController',
   templateUrl: 'views/register.html'
 })
 .when('/outbox/:id', {
   controller: 'EmailController',
   templateUrl: 'views/email.html'
 })
 .otherwise({
   redirectTo: '/Home'
 });
}]);
