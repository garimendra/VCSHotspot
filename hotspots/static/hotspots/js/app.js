(function () {
  'use strict';

  angular.module('demoApp', ['ui.tree', 'ngRoute', 'ui.bootstrap'])

    .config(['$routeProvider', '$compileProvider', function ($routeProvider, $compileProvider) {
      $routeProvider
        .when('/basic-example', {
          controller: 'BasicExampleCtrl',
          templateUrl: 'views/basic-example.html'
        });

      // testing issue #521
      $compileProvider.debugInfoEnabled(false);
    }]);
})();
