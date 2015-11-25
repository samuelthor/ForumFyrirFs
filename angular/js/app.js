var app = angular.module('HomeApp', ['ngRoute']);

app.config(['$routeProvider', function($routeProvider) {
 $routeProvider
 .when('/Home', {
   controller: 'TopicController',
   templateUrl: 'views/home.html'
 })
 .when('/Home/:id', {
   controller: 'PostController',
   templateUrl: 'views/post.html'
 })
 .when('/Login', {
  controller: 'LoginController',
  templateUrl: 'views/Login.html'
})
.when('/register', {
  controller: 'EmailController',
  templateUrl: 'views/register.html'
})
.when('/resetpassword', {
  controller: 'EmailController',
  templateUrl: 'views/resetpassword.html'
})
.when('/ucp', {
  controller: 'EmailController',
  templateUrl: 'views/ucp.html'
})
 .otherwise({
   redirectTo: '/Home'
 });
}]);
