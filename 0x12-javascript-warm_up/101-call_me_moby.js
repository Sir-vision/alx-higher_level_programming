#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  theFunction(x += 1);
};
