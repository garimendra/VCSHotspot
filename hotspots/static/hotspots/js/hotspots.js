
	var hotspotsApp = angular.module('hotspotsApp', []);

	hotspotsApp.controller('HotspotController', 
			[ '$scope', '$http', '$window', HotspotController ]);

	function HotspotController($scope, $http, $window) {

		$scope.data = [];
		$scope.score = {'score' : 0};
		$scope.loading = false;
		$scope.curDir = '//Lacerte/MainDev/WTax/';
		$scope.curFile = '';
		$scope.crumbs = []
		$scope.crumbs.push("Root");
		var shades = ["green", "green lighten-1", "green lighten-2", "green lighten-3", "red lighten-2", "red lighten-1", "red", "red darken-2", "red darken-3"];
		var	idx = Math.floor($scope.score['score']*10+0.5);
		idx = Math.min(idx, 8);
		$scope.shade = shades[idx];


		for( i=2; i < ($scope.curDir).length ; i++) {
			if ($scope.curDir[i] == '/') {
				$scope.crumbs.push($scope.curDir.substr(0, i));
			}
		}

		$scope.getChildren = function(dir) {
			$scope.data = [];
			$scope.crumbs = [];
			$scope.crumbs.push("Root");
			for( i=2; i < dir.length ; i++) {
				if (dir[i] == '/') {
					$scope.crumbs.push(dir.substr(0, i));
				}
			}

			$scope.loading = true;
			$http.get('/hotspots/fetchChildren', { params: { curDir: dir }})
				.then(function(response){
					$scope.score = {'score' : 0};
					$scope.data = response.data;
					$scope.loading = false;
				});
		}

		$scope.getScore = function(path) {
			$scope.curFile = path;
			$window.scrollTo(0,0);
			$scope.score = {'score' : 0};
			$http.get('/hotspots/fetchChildren', { params : { curDir : path }})
				.then(function(response) {
					$scope.score = response.data;
				});
			
		}

		$scope.getChildren($scope.curDir);
		
		

		$scope.handleClick = function(evt, item) {
			if(item == 'Root') {
				item = '/';
			}
			$scope.curDir = item;
			$scope.getChildren(item + '/');
			
		}

		$scope.scoreClick = function(evt, idx) {
			$scope.getScore(idx);
		}

		$scope.getClass = function() {
			var	idx = Math.floor($scope.score['score']*10+0.5);
			idx = Math.min(idx, 8);
			console.log(idx);
			$scope.shade = shades[idx];
			return "card-panel " + $scope.shade;
		}
	}




















