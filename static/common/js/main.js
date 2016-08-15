/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};

/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {

/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId])
/******/ 			return installedModules[moduleId].exports;

/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			exports: {},
/******/ 			id: moduleId,
/******/ 			loaded: false
/******/ 		};

/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);

/******/ 		// Flag the module as loaded
/******/ 		module.loaded = true;

/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}


/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;

/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;

/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";

/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(0);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ function(module, exports) {

	eval("\"use strict\";\n\n// tutorial1.js\nvar ContainerBox = React.createClass({\n    displayName: \"ContainerBox\",\n\n    render: function render() {\n        return React.createElement(\n            \"div\",\n            { className: \"containerBox\" },\n            React.createElement(Button, null),\n            React.createElement(\n                \"p\",\n                null,\n                \"sss\"\n            ),\n            React.createElement(Alert, null)\n        );\n    }\n});\n\nvar Alert = React.createClass({\n    displayName: \"Alert\",\n\n    render: function render() {\n        return React.createElement(\n            \"div\",\n            { className: \"alert alert-dismissible alert-info\" },\n            React.createElement(\n                \"button\",\n                { className: \"close\", type: \"button\", \"data-dismiss\": \"alert\" },\n                \"×\"\n            ),\n            React.createElement(\n                \"strong\",\n                null,\n                \"Heads up!\"\n            ),\n            \" This \",\n            React.createElement(\n                \"a\",\n                { href: \"#\", className: \"alert-link\" },\n                \"alert needs your attention\"\n            ),\n            \", but it's not super important.\"\n        );\n    }\n});\n\nvar Button = React.createClass({\n    displayName: \"Button\",\n\n    render: function render() {\n        return React.createElement(\n            \"a\",\n            { href: \"#\", className: \"btn btn-default\" },\n            \"Default\"\n        );\n    }\n});\nReactDOM.render(React.createElement(ContainerBox, null), document.getElementById('content-react'));\n\n/*****************\n ** WEBPACK FOOTER\n ** ./src/js/main.es6\n ** module id = 0\n ** module chunks = 0\n **/\n//# sourceURL=webpack:///./src/js/main.es6?");

/***/ }
/******/ ]);