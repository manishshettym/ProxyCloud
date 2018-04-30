/*!
 * Barlesque - ORB and all
 * Copyright (c) 2015 BBC, all rights reserved.
 */
define("orb/async/_footerpromo",["orb/lib/_$"],function(n){"use strict";var o=3e3,t=function(o,t,r){return n.addCSS(t)&&n.addHTML(o,r)},r={load:function(r,c,s){var u,e,i=s.onSuccess||function(){},a=s.onError||function(){},f=s.onAlways||function(){};u=function(n){n&&"error"!==n.status?"success"===n.status&&n.style&&n.html?t(c,n.style,n.html)?i(n):a():"none"===n.status?i(n):a():a(),f()},e={timeout:o,error:function(){a(),f()},callbackName:"navpromo"},n.script.jsonp(r,u,e)},_ioc:function(o){n=o.$}};return r});