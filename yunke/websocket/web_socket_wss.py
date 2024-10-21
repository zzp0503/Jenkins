from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import uvicorn, websocket

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
      
            (function () {
    'use strict';

    /******************************************************************************
    Copyright (c) Microsoft Corporation.

    Permission to use, copy, modify, and/or distribute this software for any
    purpose with or without fee is hereby granted.

    THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
    REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
    AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
    INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
    LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
    OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
    PERFORMANCE OF THIS SOFTWARE.
    ***************************************************************************** */
    /* global Reflect, Promise, SuppressedError, Symbol */


    function __awaiter(thisArg, _arguments, P, generator) {
        function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
        return new (P || (P = Promise))(function (resolve, reject) {
            function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
            function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
            function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
            step((generator = generator.apply(thisArg, _arguments || [])).next());
        });
    }

    function __generator(thisArg, body) {
        var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
        return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
        function verb(n) { return function (v) { return step([n, v]); }; }
        function step(op) {
            if (f) throw new TypeError("Generator is already executing.");
            while (g && (g = 0, op[0] && (_ = 0)), _) try {
                if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
                if (y = 0, t) op = [op[0] & 2, t.value];
                switch (op[0]) {
                    case 0: case 1: t = op; break;
                    case 4: _.label++; return { value: op[1], done: false };
                    case 5: _.label++; y = op[1]; op = [0]; continue;
                    case 7: op = _.ops.pop(); _.trys.pop(); continue;
                    default:
                        if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                        if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                        if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                        if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                        if (t[2]) _.ops.pop();
                        _.trys.pop(); continue;
                }
                op = body.call(thisArg, _);
            } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
            if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
        }
    }

    typeof SuppressedError === "function" ? SuppressedError : function (error, suppressed, message) {
        var e = new Error(message);
        return e.name = "SuppressedError", e.error = error, e.suppressed = suppressed, e;
    };

    /**
     *
     * 爬虫名 | （简写）
     *  Selenium (SE)
     *  Phantomjs (PH)
     *  Playwright (PL)
     *  Puppeteer / Pyppeteer (pp)
     *  DrissionPage  (DP)
     *  Puppeteer-extra / Playwright-extra (PE)
     */
    var BOT_FEATURES;
    (function (BOT_FEATURES) {
        BOT_FEATURES[BOT_FEATURES["DANGER"] = 1] = "DANGER";
        BOT_FEATURES[BOT_FEATURES["HEALTH"] = 0] = "HEALTH";
        BOT_FEATURES[BOT_FEATURES["UNDEFINED"] = -1] = "UNDEFINED";
    })(BOT_FEATURES || (BOT_FEATURES = {}));
    /**
     * 测试 userAgent 里是否包含爬虫特征
     * 命中：SE/PH/PL/PP/DP
     *
     */
    function hasUserAgent() {
        var userAgent = navigator.userAgent;
        var ua_features = ['Headless', 'PhantomJS'];
        var has = ua_features.some(function (str) { return new RegExp(str, 'i').test(userAgent); });
        return has ? BOT_FEATURES.DANGER : BOT_FEATURES.HEALTH;
    }
    /**
     * 测试 appVersion
     * 命中：SE/PH/PL/PP/DP
     */
    function hasAppVersion(resultBlock) {
        var appVersion = navigator.appVersion;
        return /headless/i.test(appVersion) ? BOT_FEATURES.DANGER : BOT_FEATURES.HEALTH;
    }
    /**
     * 浏览器语言
     * 浏览器至少包含一种语言
     */
    function hasLanguages() {
        var lan = navigator.languages;
        return lan.length === 0 ? BOT_FEATURES.DANGER : BOT_FEATURES.HEALTH;
    }
    /**
     *
     *  navigator.webdriver 为 true 是 爬虫
     */
    function hasWebdriver() {
        return navigator.webdriver ? BOT_FEATURES.DANGER : BOT_FEATURES.HEALTH;
    }
    /**
     * 测试dom
     * @returns
     */
    function hasWebdriverDocumentAttribute() {
        var documentAttributeKeys = [
            "__webdriver_script_func",
            "__webdriver_script_function",
            "webdriver",
            "_Selenium_IDE_Recorder",
            "_selenium",
            "calledSelenium",
            "_WEBDRIVER_ELEM_CACHE",
            "ChromeDriverw",
            "driver-evaluate",
            "webdriver-evaluate",
            "selenium-evaluate",
            "webdriverCommand",
            "webdriver-evaluate-response",
            "__webdriverFunc",
            "__$webdriverAsyncExecutor",
            "__lastWatirAlert",
            "__lastWatirConfirm",
            "__lastWatirPrompt",
            "$chrome_asyncScriptInfo",
            "$cdc_asdjflasutopfhvcZLmcfl_"
        ];
        var documentElementAttributeKeys = [
            "selenium",
            "webdriver",
            "driver"
        ];
        var result = documentAttributeKeys.some(function (key) { return !!window.document[key]; }) || documentElementAttributeKeys.some(function (key) { return !!window.document.documentElement.getAttribute(key); });
        return result ? BOT_FEATURES.DANGER : BOT_FEATURES.HEALTH;
    }
    function hasWindowAttribute() {
        var windowAttributeKeys = [
            "_phantom",
            "__nightmare",
            "_selenium",
            "callPhantom",
            "callSelenium",
            "_Selenium_IDE_Recorder",
        ];
        var isHasAttribute = windowAttributeKeys.some(function (key) { return !!window[key]; });
        if (isHasAttribute)
            return BOT_FEATURES.DANGER;
        if (window.external && window.external.toString() && (window.external.toString().indexOf("Sequentum") !== -1)) {
            return BOT_FEATURES.DANGER;
        }
        return BOT_FEATURES.HEALTH;
    }
    function hasCDCAttribute() {
        var matches = [];
        for (var prop in window) {
            prop.match(/cdc_\S/ig) && matches.push(prop);
        }
        function hasvarructorAlias(window, varructor) {
            for (var _i = 0, _a = window.Object.getOwnPropertyNames(window); _i < _a.length; _i++) {
                var prop = _a[_i];
                if (prop === varructor.name)
                    continue;
                if (window[prop] === varructor)
                    return true;
            }
            return false;
        }
        var testResult = hasvarructorAlias(window, window.Array)
            && hasvarructorAlias(window, window.Promise)
            && hasvarructorAlias(window, window.Symbol)
            && matches.length > 0;
        return testResult ? BOT_FEATURES.DANGER : BOT_FEATURES.HEALTH;
    }
    function hasChrome() {
        var chrome = window['chrome'];
        var userAgent = navigator.userAgent;
        if (userAgent.indexOf("WebKit") !== -1) {
            return chrome ? BOT_FEATURES.HEALTH : BOT_FEATURES.DANGER;
        }
        return BOT_FEATURES.HEALTH;
    }
    /**
     *  正常值
     *  Notification.permission = default 、
     *  var permissionStatus = navigator.permissions.query({name: "notifications"})
     *  permissionStatus.state = prompt；
     * @returns
     */
    function hasPermission() {
        return __awaiter(this, void 0, void 0, function () {
            var permissionStatus, notificationPermission;
            return __generator(this, function (_a) {
                switch (_a.label) {
                    case 0:
                        if (navigator.permissions)
                            return [2 /*return*/, BOT_FEATURES.UNDEFINED];
                        _a.label = 1;
                    case 1:
                        _a.trys.push([1, 3, , 4]);
                        return [4 /*yield*/, navigator.permissions.query({ name: "notifications" })];
                    case 2:
                        permissionStatus = _a.sent();
                        notificationPermission = Notification.permission;
                        if (notificationPermission === "denied" && permissionStatus.state === "prompt") {
                            return [2 /*return*/, BOT_FEATURES.DANGER];
                        }
                        return [2 /*return*/, BOT_FEATURES.HEALTH];
                    case 3:
                        _a.sent();
                        return [2 /*return*/, BOT_FEATURES.DANGER];
                    case 4: return [2 /*return*/];
                }
            });
        });
    }
    /**
     * 通过插件判断
     * 插件长度为0 判定为爬虫；
     *
     * @returns
     */
    function hasPluginsLength() {
        var plugins = navigator.plugins ? navigator.plugins : [];
        if (plugins.length === 0)
            return BOT_FEATURES.DANGER;
        var prototypeTest = PluginArray.prototype === navigator.plugins['__proto__'] && Plugin.prototype === navigator.plugins[0]['__proto__'];
        var typeTest = navigator.plugins instanceof PluginArray && navigator.plugins[0].toString() === '[object Plugin]';
        return prototypeTest && typeTest ? BOT_FEATURES.HEALTH : BOT_FEATURES.DANGER;
    }
    /**
     * 正常值 avigator.mimeTypes.length > 0
     */
    function hasMimeTypesLength() {
        return navigator.mimeTypes.length ? BOT_FEATURES.HEALTH : BOT_FEATURES.DANGER;
    }
    function testMimeTypesPrototypeAndType() {
        var mimeTypesLength = navigator.mimeTypes.length;
        if (mimeTypesLength === 0) {
            return BOT_FEATURES.DANGER;
        }
        else {
            var prototypeTest = MimeTypeArray.prototype === navigator.mimeTypes['__proto__'] && MimeType.prototype === navigator.mimeTypes[0]['__proto__'];
            var typeTest = navigator.mimeTypes instanceof MimeTypeArray && navigator.mimeTypes[0].toString() === '[object MimeType]';
            return prototypeTest && typeTest ? BOT_FEATURES.HEALTH : BOT_FEATURES.DANGER;
        }
    }
    /**
     * 网络测试
     * @returns
     */
    function testConnectionRtt() {
        var connection = navigator['connection'];
        var connectionRtt = connection ? connection.rtt : undefined;
        if (connectionRtt === undefined) {
            return BOT_FEATURES.UNDEFINED;
        }
        else {
            return connectionRtt === 0 ? BOT_FEATURES.DANGER : BOT_FEATURES.HEALTH;
        }
    }
    /**
     * WebGL Vendor
     * vendor === "Brian Paul" || vendor === "Google Inc."
     * WebGL Renderer
     * renderer === "Mesa OffScreen" || renderer.indexOf("Swift") !== -1
     * @returns
     */
    function hasWebGLVendor() {
        var canvas = document.createElement("canvas");
        var gl = canvas.getContext("webgl") || canvas.getContext("webgl-experimental");
        if (gl) {
            var debugInfo = gl.getExtension("WEBGL_debug_renderer_info");
            try {
                var vendor = gl.getParameter(debugInfo.UNMASKED_VENDOR_WEBGL);
                var renderer = gl.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL);
                if (vendor === "Brian Paul" || vendor === "Google Inc.") {
                    return BOT_FEATURES.DANGER;
                }
                else if (renderer === "Mesa OffScreen" || renderer.indexOf("Swift") !== -1) {
                    return BOT_FEATURES.DANGER;
                }
                else {
                    return BOT_FEATURES.HEALTH;
                }
            }
            catch (e) {
                return BOT_FEATURES.UNDEFINED;
            }
        }
        else {
            return BOT_FEATURES.DANGER;
        }
    }
    /**
     * 窗口大小测试
     * @returns
     */
    function hasScreenSize() {
        var width = screen.width;
        var height = screen.height;
        var availWidth = screen.availWidth;
        var availHeight = screen.availHeight;
        var outerWidth = window.outerWidth;
        var outerHeight = window.outerHeight;
        var innerWidth = window.innerWidth;
        var innerHeight = window.innerHeight;
        var testResult = width !== 0 && height !== 0 &&
            availWidth !== 0 && availHeight !== 0 && outerWidth !== 0 &&
            outerHeight !== 0 && innerWidth !== 0 && outerWidth !== 0 &&
            width >= availWidth && height >= availHeight &&
            outerWidth >= innerWidth && outerHeight >= innerHeight;
        return testResult ? BOT_FEATURES.HEALTH : BOT_FEATURES.DANGER;
    }
    /**
     * https://github.com/puppeteer/puppeteer/issues/1106
     * https://github.com/paulirish/headless-cat-n-mouse/blob/master/detect-headless.js
     * https://github.com/berstend/puppeteer-extra/tree/master/packages/puppeteer-extra-plugin-stealth/evasions/iframe.contentWindow
     *
     * 测试IFrame
     *
     * @returns
     */
    function testIFrame() {
        window['iframeTestFlag'] = "true";
        var srcdocIframe = (function () {
            var el = document.createElement("iframe");
            el.srcdoc = "Puppeteer Extra Test";
            document.head.appendChild(el);
            var flag = el.contentWindow['iframeTestFlag'];
            document.head.removeChild(el);
            return flag;
        })();
        return srcdocIframe === undefined ? BOT_FEATURES.HEALTH : BOT_FEATURES.DANGER;
    }

    var hasBot = /*#__PURE__*/Object.freeze({
        __proto__: null,
        hasAppVersion: hasAppVersion,
        hasCDCAttribute: hasCDCAttribute,
        hasChrome: hasChrome,
        hasLanguages: hasLanguages,
        hasMimeTypesLength: hasMimeTypesLength,
        hasPermission: hasPermission,
        hasPluginsLength: hasPluginsLength,
        hasScreenSize: hasScreenSize,
        hasUserAgent: hasUserAgent,
        hasWebGLVendor: hasWebGLVendor,
        hasWebdriver: hasWebdriver,
        hasWebdriverDocumentAttribute: hasWebdriverDocumentAttribute,
        hasWindowAttribute: hasWindowAttribute,
        testConnectionRtt: testConnectionRtt,
        testIFrame: testIFrame,
        testMimeTypesPrototypeAndType: testMimeTypesPrototypeAndType
    });

    var prohibitedPluginLibrary = [
        {
            id: 'mooikfkahbdckldjjndioackbalphokd',
            url: 'chrome-extension://mooikfkahbdckldjjndioackbalphokd/assets/prompt.js'
        }
    ];
    function checkPlugin(plugin) {
        var url = plugin.url;
        return new Promise(function (resolve, reject) {
            var xml = new XMLHttpRequest();
            xml.open('get', url);
            xml.onreadystatechange = function () {
                if (xml.readyState == 4) {
                    if (xml.status == 200) {
                        resolve(xml.responseText);
                    }
                    else {
                        reject();
                    }
                }
            };
            xml.send();
        });
    }
    function pluginCheck () {
        return Promise.allSettled(prohibitedPluginLibrary.map(checkPlugin));
    }

    /**
     *
     * @param name  cookie key 名
     * @param value cookie value名
     * @param expires c
     * @param path
     * @param domain
     */
    function setCookie(name, value, expires, path, domain) {
        var cookieString = name + "=" + encodeURIComponent(value);
        if (expires) {
            cookieString += ";expires=" + expires.toUTCString();
        }
        if (path) {
            cookieString += ";path=" + path;
        }
        if (domain) {
            cookieString += ";domain=" + domain;
        }
        document.cookie = cookieString;
    }
    function getCookie(name) {
        var cookies = document.cookie.split("; ");
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].split("=");
            if (cookie[0] === name) {
                return decodeURIComponent(cookie[1]);
            }
        }
        return "";
    }

    function _toPrimitive(t, r) {
      if ("object" != typeof t || !t) return t;
      var e = t[Symbol.toPrimitive];
      if (void 0 !== e) {
        var i = e.call(t, r || "default");
        if ("object" != typeof i) return i;
        throw new TypeError("@@toPrimitive must return a primitive value.");
      }
      return ("string" === r ? String : Number)(t);
    }
    function _toPropertyKey(t) {
      var i = _toPrimitive(t, "string");
      return "symbol" == typeof i ? i : String(i);
    }
    function _defineProperty(obj, key, value) {
      key = _toPropertyKey(key);
      if (key in obj) {
        Object.defineProperty(obj, key, {
          value: value,
          enumerable: true,
          configurable: true,
          writable: true
        });
      } else {
        obj[key] = value;
      }
      return obj;
    }

    var _ref, _ref2, _ref3, _ref4, _ref5;
    /* eslint-disable no-use-before-define */

    const crypto = ((_ref = typeof globalThis != 'undefined' ? globalThis : void 0) === null || _ref === void 0 ? void 0 : _ref.crypto) || ((_ref2 = typeof global != 'undefined' ? global : void 0) === null || _ref2 === void 0 ? void 0 : _ref2.crypto) || ((_ref3 = typeof window != 'undefined' ? window : void 0) === null || _ref3 === void 0 ? void 0 : _ref3.crypto) || ((_ref4 = typeof self != 'undefined' ? self : void 0) === null || _ref4 === void 0 ? void 0 : _ref4.crypto) || ((_ref5 = typeof frames != 'undefined' ? frames : void 0) === null || _ref5 === void 0 || (_ref5 = _ref5[0]) === null || _ref5 === void 0 ? void 0 : _ref5.crypto);
    let randomWordArray;
    if (crypto) {
      randomWordArray = nBytes => {
        const words = [];
        for (let i = 0, rcache; i < nBytes; i += 4) {
          words.push(crypto.getRandomValues(new Uint32Array(1))[0]);
        }
        return new WordArray(words, nBytes);
      };
    } else {
      // Because there is no global crypto property in this context, cryptographically unsafe Math.random() is used.

      randomWordArray = nBytes => {
        const words = [];
        const r = m_w => {
          let _m_w = m_w;
          let _m_z = 0x3ade68b1;
          const mask = 0xffffffff;
          return () => {
            _m_z = 0x9069 * (_m_z & 0xFFFF) + (_m_z >> 0x10) & mask;
            _m_w = 0x4650 * (_m_w & 0xFFFF) + (_m_w >> 0x10) & mask;
            let result = (_m_z << 0x10) + _m_w & mask;
            result /= 0x100000000;
            result += 0.5;
            return result * (Math.random() > 0.5 ? 1 : -1);
          };
        };
        for (let i = 0, rcache; i < nBytes; i += 4) {
          const _r = r((rcache || Math.random()) * 0x100000000);
          rcache = _r() * 0x3ade67b7;
          words.push(_r() * 0x100000000 | 0);
        }
        return new WordArray(words, nBytes);
      };
    }

    /**
     * Base class for inheritance.
     */
    class Base {
      /**
       * Extends this object and runs the init method.
       * Arguments to create() will be passed to init().
       *
       * @return {Object} The new object.
       *
       * @static
       *
       * @example
       *
       *     var instance = MyType.create();
       */
      static create(...args) {
        return new this(...args);
      }

      /**
       * Copies properties into this object.
       *
       * @param {Object} properties The properties to mix in.
       *
       * @example
       *
       *     MyType.mixIn({
       *         field: 'value'
       *     });
       */
      mixIn(properties) {
        return Object.assign(this, properties);
      }

      /**
       * Creates a copy of this object.
       *
       * @return {Object} The clone.
       *
       * @example
       *
       *     var clone = instance.clone();
       */
      clone() {
        const clone = new this.constructor();
        Object.assign(clone, this);
        return clone;
      }
    }

    /**
     * An array of 32-bit words.
     *
     * @property {Array} words The array of 32-bit words.
     * @property {number} sigBytes The number of significant bytes in this word array.
     */
    class WordArray extends Base {
      /**
       * Initializes a newly created word array.
       *
       * @param {Array} words (Optional) An array of 32-bit words.
       * @param {number} sigBytes (Optional) The number of significant bytes in the words.
       *
       * @example
       *
       *     var wordArray = CryptoJS.lib.WordArray.create();
       *     var wordArray = CryptoJS.lib.WordArray.create([0x00010203, 0x04050607]);
       *     var wordArray = CryptoJS.lib.WordArray.create([0x00010203, 0x04050607], 6);
       */
      constructor(words = [], sigBytes = words.length * 4) {
        super();
        let typedArray = words;
        // Convert buffers to uint8
        if (typedArray instanceof ArrayBuffer) {
          typedArray = new Uint8Array(typedArray);
        }

        // Convert other array views to uint8
        if (typedArray instanceof Int8Array || typedArray instanceof Uint8ClampedArray || typedArray instanceof Int16Array || typedArray instanceof Uint16Array || typedArray instanceof Int32Array || typedArray instanceof Uint32Array || typedArray instanceof Float32Array || typedArray instanceof Float64Array) {
          typedArray = new Uint8Array(typedArray.buffer, typedArray.byteOffset, typedArray.byteLength);
        }

        // Handle Uint8Array
        if (typedArray instanceof Uint8Array) {
          // Shortcut
          const typedArrayByteLength = typedArray.byteLength;

          // Extract bytes
          const _words = [];
          for (let i = 0; i < typedArrayByteLength; i += 1) {
            _words[i >>> 2] |= typedArray[i] << 24 - i % 4 * 8;
          }

          // Initialize this word array
          this.words = _words;
          this.sigBytes = typedArrayByteLength;
        } else {
          // Else call normal init
          this.words = words;
          this.sigBytes = sigBytes;
        }
      }

      /**
       * Creates a word array filled with random bytes.
       *
       * @param {number} nBytes The number of random bytes to generate.
       *
       * @return {WordArray} The random word array.
       *
       * @static
       *
       * @example
       *
       *     var wordArray = CryptoJS.lib.WordArray.random(16);
       */

      /**
       * Converts this word array to a string.
       *
       * @param {Encoder} encoder (Optional) The encoding strategy to use. Default: CryptoJS.enc.Hex
       *
       * @return {string} The stringified word array.
       *
       * @example
       *
       *     var string = wordArray + '';
       *     var string = wordArray.toString();
       *     var string = wordArray.toString(CryptoJS.enc.Utf8);
       */
      toString(encoder = Hex) {
        return encoder.stringify(this);
      }

      /**
       * Concatenates a word array to this word array.
       *
       * @param {WordArray} wordArray The word array to append.
       *
       * @return {WordArray} This word array.
       *
       * @example
       *
       *     wordArray1.concat(wordArray2);
       */
      concat(wordArray) {
        // Shortcuts
        const thisWords = this.words;
        const thatWords = wordArray.words;
        const thisSigBytes = this.sigBytes;
        const thatSigBytes = wordArray.sigBytes;

        // Clamp excess bits
        this.clamp();

        // Concat
        if (thisSigBytes % 4) {
          // Copy one byte at a time
          for (let i = 0; i < thatSigBytes; i += 1) {
            const thatByte = thatWords[i >>> 2] >>> 24 - i % 4 * 8 & 0xff;
            thisWords[thisSigBytes + i >>> 2] |= thatByte << 24 - (thisSigBytes + i) % 4 * 8;
          }
        } else {
          // Copy one word at a time
          for (let i = 0; i < thatSigBytes; i += 4) {
            thisWords[thisSigBytes + i >>> 2] = thatWords[i >>> 2];
          }
        }
        this.sigBytes += thatSigBytes;

        // Chainable
        return this;
      }

      /**
       * Removes insignificant bits.
       *
       * @example
       *
       *     wordArray.clamp();
       */
      clamp() {
        // Shortcuts
        const {
          words,
          sigBytes
        } = this;

        // Clamp
        words[sigBytes >>> 2] &= 0xffffffff << 32 - sigBytes % 4 * 8;
        words.length = Math.ceil(sigBytes / 4);
      }

      /**
       * Creates a copy of this word array.
       *
       * @return {WordArray} The clone.
       *
       * @example
       *
       *     var clone = wordArray.clone();
       */
      clone() {
        const clone = super.clone.call(this);
        clone.words = this.words.slice(0);
        return clone;
      }
    }

    /**
     * Hex encoding strategy.
     */
    _defineProperty(WordArray, "random", randomWordArray);
    const Hex = {
      /**
       * Converts a word array to a hex string.
       *
       * @param {WordArray} wordArray The word array.
       *
       * @return {string} The hex string.
       *
       * @static
       *
       * @example
       *
       *     var hexString = CryptoJS.enc.Hex.stringify(wordArray);
       */
      stringify(wordArray) {
        // Shortcuts
        const {
          words,
          sigBytes
        } = wordArray;

        // Convert
        const hexChars = [];
        for (let i = 0; i < sigBytes; i += 1) {
          const bite = words[i >>> 2] >>> 24 - i % 4 * 8 & 0xff;
          hexChars.push((bite >>> 4).toString(16));
          hexChars.push((bite & 0x0f).toString(16));
        }
        return hexChars.join('');
      },
      /**
       * Converts a hex string to a word array.
       *
       * @param {string} hexStr The hex string.
       *
       * @return {WordArray} The word array.
       *
       * @static
       *
       * @example
       *
       *     var wordArray = CryptoJS.enc.Hex.parse(hexString);
       */
      parse(hexStr) {
        // Shortcut
        const hexStrLength = hexStr.length;

        // Convert
        const words = [];
        for (let i = 0; i < hexStrLength; i += 2) {
          words[i >>> 3] |= parseInt(hexStr.substr(i, 2), 16) << 24 - i % 8 * 4;
        }
        return new WordArray(words, hexStrLength / 2);
      }
    };

    /**
     * Latin1 encoding strategy.
     */
    const Latin1 = {
      /**
       * Converts a word array to a Latin1 string.
       *
       * @param {WordArray} wordArray The word array.
       *
       * @return {string} The Latin1 string.
       *
       * @static
       *
       * @example
       *
       *     var latin1String = CryptoJS.enc.Latin1.stringify(wordArray);
       */
      stringify(wordArray) {
        // Shortcuts
        const {
          words,
          sigBytes
        } = wordArray;

        // Convert
        const latin1Chars = [];
        for (let i = 0; i < sigBytes; i += 1) {
          const bite = words[i >>> 2] >>> 24 - i % 4 * 8 & 0xff;
          latin1Chars.push(String.fromCharCode(bite));
        }
        return latin1Chars.join('');
      },
      /**
       * Converts a Latin1 string to a word array.
       *
       * @param {string} latin1Str The Latin1 string.
       *
       * @return {WordArray} The word array.
       *
       * @static
       *
       * @example
       *
       *     var wordArray = CryptoJS.enc.Latin1.parse(latin1String);
       */
      parse(latin1Str) {
        // Shortcut
        const latin1StrLength = latin1Str.length;

        // Convert
        const words = [];
        for (let i = 0; i < latin1StrLength; i += 1) {
          words[i >>> 2] |= (latin1Str.charCodeAt(i) & 0xff) << 24 - i % 4 * 8;
        }
        return new WordArray(words, latin1StrLength);
      }
    };

    /**
     * UTF-8 encoding strategy.
     */
    const Utf8 = {
      /**
       * Converts a word array to a UTF-8 string.
       *
       * @param {WordArray} wordArray The word array.
       *
       * @return {string} The UTF-8 string.
       *
       * @static
       *
       * @example
       *
       *     var utf8String = CryptoJS.enc.Utf8.stringify(wordArray);
       */
      stringify(wordArray) {
        try {
          return decodeURIComponent(escape(Latin1.stringify(wordArray)));
        } catch (e) {
          throw new Error('Malformed UTF-8 data');
        }
      },
      /**
       * Converts a UTF-8 string to a word array.
       *
       * @param {string} utf8Str The UTF-8 string.
       *
       * @return {WordArray} The word array.
       *
       * @static
       *
       * @example
       *
       *     var wordArray = CryptoJS.enc.Utf8.parse(utf8String);
       */
      parse(utf8Str) {
        return Latin1.parse(unescape(encodeURIComponent(utf8Str)));
      }
    };

    /**
     * Abstract buffered block algorithm template.
     *
     * The property blockSize must be implemented in a concrete subtype.
     *
     * @property {number} _minBufferSize
     *
     *     The number of blocks that should be kept unprocessed in the buffer. Default: 0
     */
    class BufferedBlockAlgorithm extends Base {
      constructor() {
        super();
        this._minBufferSize = 0;
      }

      /**
       * Resets this block algorithm's data buffer to its initial state.
       *
       * @example
       *
       *     bufferedBlockAlgorithm.reset();
       */
      reset() {
        // Initial values
        this._data = new WordArray();
        this._nDataBytes = 0;
      }

      /**
       * Adds new data to this block algorithm's buffer.
       *
       * @param {WordArray|string} data
       *
       *     The data to append. Strings are converted to a WordArray using UTF-8.
       *
       * @example
       *
       *     bufferedBlockAlgorithm._append('data');
       *     bufferedBlockAlgorithm._append(wordArray);
       */
      _append(data) {
        let m_data = data;

        // Convert string to WordArray, else assume WordArray already
        if (typeof m_data === 'string') {
          m_data = Utf8.parse(m_data);
        }

        // Append
        this._data.concat(m_data);
        this._nDataBytes += m_data.sigBytes;
      }

      /**
       * Processes available data blocks.
       *
       * This method invokes _doProcessBlock(offset), which must be implemented by a concrete subtype.
       *
       * @param {boolean} doFlush Whether all blocks and partial blocks should be processed.
       *
       * @return {WordArray} The processed data.
       *
       * @example
       *
       *     var processedData = bufferedBlockAlgorithm._process();
       *     var processedData = bufferedBlockAlgorithm._process(!!'flush');
       */
      _process(doFlush) {
        let processedWords;

        // Shortcuts
        const {
          _data: data,
          blockSize
        } = this;
        const dataWords = data.words;
        const dataSigBytes = data.sigBytes;
        const blockSizeBytes = blockSize * 4;

        // Count blocks ready
        let nBlocksReady = dataSigBytes / blockSizeBytes;
        if (doFlush) {
          // Round up to include partial blocks
          nBlocksReady = Math.ceil(nBlocksReady);
        } else {
          // Round down to include only full blocks,
          // less the number of blocks that must remain in the buffer
          nBlocksReady = Math.max((nBlocksReady | 0) - this._minBufferSize, 0);
        }

        // Count words ready
        const nWordsReady = nBlocksReady * blockSize;

        // Count bytes ready
        const nBytesReady = Math.min(nWordsReady * 4, dataSigBytes);

        // Process blocks
        if (nWordsReady) {
          for (let offset = 0; offset < nWordsReady; offset += blockSize) {
            // Perform concrete-algorithm logic
            this._doProcessBlock(dataWords, offset);
          }

          // Remove processed words
          processedWords = dataWords.splice(0, nWordsReady);
          data.sigBytes -= nBytesReady;
        }

        // Return processed words
        return new WordArray(processedWords, nBytesReady);
      }

      /**
       * Creates a copy of this object.
       *
       * @return {Object} The clone.
       *
       * @example
       *
       *     var clone = bufferedBlockAlgorithm.clone();
       */
      clone() {
        const clone = super.clone.call(this);
        clone._data = this._data.clone();
        return clone;
      }
    }

    /**
     * Abstract hasher template.
     *
     * @property {number} blockSize
     *
     *     The number of 32-bit words this hasher operates on. Default: 16 (512 bits)
     */
    class Hasher extends BufferedBlockAlgorithm {
      constructor(cfg) {
        super();
        this.blockSize = 512 / 32;

        /**
         * Configuration options.
         */
        this.cfg = Object.assign(new Base(), cfg);

        // Set initial values
        this.reset();
      }

      /**
       * Creates a shortcut function to a hasher's object interface.
       *
       * @param {Hasher} SubHasher The hasher to create a helper for.
       *
       * @return {Function} The shortcut function.
       *
       * @static
       *
       * @example
       *
       *     var SHA256 = CryptoJS.lib.Hasher._createHelper(CryptoJS.algo.SHA256);
       */
      static _createHelper(SubHasher) {
        return (message, cfg) => new SubHasher(cfg).finalize(message);
      }

      /**
       * Creates a shortcut function to the HMAC's object interface.
       *
       * @param {Hasher} SubHasher The hasher to use in this HMAC helper.
       *
       * @return {Function} The shortcut function.
       *
       * @static
       *
       * @example
       *
       *     var HmacSHA256 = CryptoJS.lib.Hasher._createHmacHelper(CryptoJS.algo.SHA256);
       */
      static _createHmacHelper(SubHasher) {
        return (message, key) => new HMAC(SubHasher, key).finalize(message);
      }

      /**
       * Resets this hasher to its initial state.
       *
       * @example
       *
       *     hasher.reset();
       */
      reset() {
        // Reset data buffer
        super.reset.call(this);

        // Perform concrete-hasher logic
        this._doReset();
      }

      /**
       * Updates this hasher with a message.
       *
       * @param {WordArray|string} messageUpdate The message to append.
       *
       * @return {Hasher} This hasher.
       *
       * @example
       *
       *     hasher.update('message');
       *     hasher.update(wordArray);
       */
      update(messageUpdate) {
        // Append
        this._append(messageUpdate);

        // Update the hash
        this._process();

        // Chainable
        return this;
      }

      /**
       * Finalizes the hash computation.
       * Note that the finalize operation is effectively a destructive, read-once operation.
       *
       * @param {WordArray|string} messageUpdate (Optional) A final message update.
       *
       * @return {WordArray} The hash.
       *
       * @example
       *
       *     var hash = hasher.finalize();
       *     var hash = hasher.finalize('message');
       *     var hash = hasher.finalize(wordArray);
       */
      finalize(messageUpdate) {
        // Final message update
        if (messageUpdate) {
          this._append(messageUpdate);
        }

        // Perform concrete-hasher logic
        const hash = this._doFinalize();
        return hash;
      }
    }

    /**
     * HMAC algorithm.
     */
    class HMAC extends Base {
      /**
       * Initializes a newly created HMAC.
       *
       * @param {Hasher} SubHasher The hash algorithm to use.
       * @param {WordArray|string} key The secret key.
       *
       * @example
       *
       *     var hmacHasher = CryptoJS.algo.HMAC.create(CryptoJS.algo.SHA256, key);
       */
      constructor(SubHasher, key) {
        super();
        const hasher = new SubHasher();
        this._hasher = hasher;

        // Convert string to WordArray, else assume WordArray already
        let _key = key;
        if (typeof _key === 'string') {
          _key = Utf8.parse(_key);
        }

        // Shortcuts
        const hasherBlockSize = hasher.blockSize;
        const hasherBlockSizeBytes = hasherBlockSize * 4;

        // Allow arbitrary length keys
        if (_key.sigBytes > hasherBlockSizeBytes) {
          _key = hasher.finalize(key);
        }

        // Clamp excess bits
        _key.clamp();

        // Clone key for inner and outer pads
        const oKey = _key.clone();
        this._oKey = oKey;
        const iKey = _key.clone();
        this._iKey = iKey;

        // Shortcuts
        const oKeyWords = oKey.words;
        const iKeyWords = iKey.words;

        // XOR keys with pad constants
        for (let i = 0; i < hasherBlockSize; i += 1) {
          oKeyWords[i] ^= 0x5c5c5c5c;
          iKeyWords[i] ^= 0x36363636;
        }
        oKey.sigBytes = hasherBlockSizeBytes;
        iKey.sigBytes = hasherBlockSizeBytes;

        // Set initial values
        this.reset();
      }

      /**
       * Resets this HMAC to its initial state.
       *
       * @example
       *
       *     hmacHasher.reset();
       */
      reset() {
        // Shortcut
        const hasher = this._hasher;

        // Reset
        hasher.reset();
        hasher.update(this._iKey);
      }

      /**
       * Updates this HMAC with a message.
       *
       * @param {WordArray|string} messageUpdate The message to append.
       *
       * @return {HMAC} This HMAC instance.
       *
       * @example
       *
       *     hmacHasher.update('message');
       *     hmacHasher.update(wordArray);
       */
      update(messageUpdate) {
        this._hasher.update(messageUpdate);

        // Chainable
        return this;
      }

      /**
       * Finalizes the HMAC computation.
       * Note that the finalize operation is effectively a destructive, read-once operation.
       *
       * @param {WordArray|string} messageUpdate (Optional) A final message update.
       *
       * @return {WordArray} The HMAC.
       *
       * @example
       *
       *     var hmac = hmacHasher.finalize();
       *     var hmac = hmacHasher.finalize('message');
       *     var hmac = hmacHasher.finalize(wordArray);
       */
      finalize(messageUpdate) {
        // Shortcut
        const hasher = this._hasher;

        // Compute HMAC
        const innerHash = hasher.finalize(messageUpdate);
        hasher.reset();
        const hmac = hasher.finalize(this._oKey.clone().concat(innerHash));
        return hmac;
      }
    }

    const parseLoop = (base64Str, base64StrLength, reverseMap) => {
      const words = [];
      let nBytes = 0;
      for (let i = 0; i < base64StrLength; i += 1) {
        if (i % 4) {
          const bits1 = reverseMap[base64Str.charCodeAt(i - 1)] << i % 4 * 2;
          const bits2 = reverseMap[base64Str.charCodeAt(i)] >>> 6 - i % 4 * 2;
          const bitsCombined = bits1 | bits2;
          words[nBytes >>> 2] |= bitsCombined << 24 - nBytes % 4 * 8;
          nBytes += 1;
        }
      }
      return WordArray.create(words, nBytes);
    };

    /**
     * Base64 encoding strategy.
     */
    const Base64 = {
      /**
       * Converts a word array to a Base64 string.
       *
       * @param {WordArray} wordArray The word array.
       *
       * @return {string} The Base64 string.
       *
       * @static
       *
       * @example
       *
       *     const base64String = CryptoJS.enc.Base64.stringify(wordArray);
       */
      stringify(wordArray) {
        // Shortcuts
        const {
          words,
          sigBytes
        } = wordArray;
        const map = this._map;

        // Clamp excess bits
        wordArray.clamp();

        // Convert
        const base64Chars = [];
        for (let i = 0; i < sigBytes; i += 3) {
          const byte1 = words[i >>> 2] >>> 24 - i % 4 * 8 & 0xff;
          const byte2 = words[i + 1 >>> 2] >>> 24 - (i + 1) % 4 * 8 & 0xff;
          const byte3 = words[i + 2 >>> 2] >>> 24 - (i + 2) % 4 * 8 & 0xff;
          const triplet = byte1 << 16 | byte2 << 8 | byte3;
          for (let j = 0; j < 4 && i + j * 0.75 < sigBytes; j += 1) {
            base64Chars.push(map.charAt(triplet >>> 6 * (3 - j) & 0x3f));
          }
        }

        // Add padding
        const paddingChar = map.charAt(64);
        if (paddingChar) {
          while (base64Chars.length % 4) {
            base64Chars.push(paddingChar);
          }
        }
        return base64Chars.join('');
      },
      /**
       * Converts a Base64 string to a word array.
       *
       * @param {string} base64Str The Base64 string.
       *
       * @return {WordArray} The word array.
       *
       * @static
       *
       * @example
       *
       *     const wordArray = CryptoJS.enc.Base64.parse(base64String);
       */
      parse(base64Str) {
        // Shortcuts
        let base64StrLength = base64Str.length;
        const map = this._map;
        let reverseMap = this._reverseMap;
        if (!reverseMap) {
          this._reverseMap = [];
          reverseMap = this._reverseMap;
          for (let j = 0; j < map.length; j += 1) {
            reverseMap[map.charCodeAt(j)] = j;
          }
        }

        // Ignore padding
        const paddingChar = map.charAt(64);
        if (paddingChar) {
          const paddingIndex = base64Str.indexOf(paddingChar);
          if (paddingIndex !== -1) {
            base64StrLength = paddingIndex;
          }
        }

        // Convert
        return parseLoop(base64Str, base64StrLength, reverseMap);
      },
      _map: 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
    };

    // Constants table
    const T = [];

    // Compute constants
    for (let i = 0; i < 64; i += 1) {
      T[i] = Math.abs(Math.sin(i + 1)) * 0x100000000 | 0;
    }
    const FF = (a, b, c, d, x, s, t) => {
      const n = a + (b & c | ~b & d) + x + t;
      return (n << s | n >>> 32 - s) + b;
    };
    const GG = (a, b, c, d, x, s, t) => {
      const n = a + (b & d | c & ~d) + x + t;
      return (n << s | n >>> 32 - s) + b;
    };
    const HH = (a, b, c, d, x, s, t) => {
      const n = a + (b ^ c ^ d) + x + t;
      return (n << s | n >>> 32 - s) + b;
    };
    const II = (a, b, c, d, x, s, t) => {
      const n = a + (c ^ (b | ~d)) + x + t;
      return (n << s | n >>> 32 - s) + b;
    };

    /**
     * MD5 hash algorithm.
     */
    class MD5Algo extends Hasher {
      _doReset() {
        this._hash = new WordArray([0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476]);
      }
      _doProcessBlock(M, offset) {
        const _M = M;

        // Swap endian
        for (let i = 0; i < 16; i += 1) {
          // Shortcuts
          const offset_i = offset + i;
          const M_offset_i = M[offset_i];
          _M[offset_i] = (M_offset_i << 8 | M_offset_i >>> 24) & 0x00ff00ff | (M_offset_i << 24 | M_offset_i >>> 8) & 0xff00ff00;
        }

        // Shortcuts
        const H = this._hash.words;
        const M_offset_0 = _M[offset + 0];
        const M_offset_1 = _M[offset + 1];
        const M_offset_2 = _M[offset + 2];
        const M_offset_3 = _M[offset + 3];
        const M_offset_4 = _M[offset + 4];
        const M_offset_5 = _M[offset + 5];
        const M_offset_6 = _M[offset + 6];
        const M_offset_7 = _M[offset + 7];
        const M_offset_8 = _M[offset + 8];
        const M_offset_9 = _M[offset + 9];
        const M_offset_10 = _M[offset + 10];
        const M_offset_11 = _M[offset + 11];
        const M_offset_12 = _M[offset + 12];
        const M_offset_13 = _M[offset + 13];
        const M_offset_14 = _M[offset + 14];
        const M_offset_15 = _M[offset + 15];

        // Working varialbes
        let a = H[0];
        let b = H[1];
        let c = H[2];
        let d = H[3];

        // Computation
        a = FF(a, b, c, d, M_offset_0, 7, T[0]);
        d = FF(d, a, b, c, M_offset_1, 12, T[1]);
        c = FF(c, d, a, b, M_offset_2, 17, T[2]);
        b = FF(b, c, d, a, M_offset_3, 22, T[3]);
        a = FF(a, b, c, d, M_offset_4, 7, T[4]);
        d = FF(d, a, b, c, M_offset_5, 12, T[5]);
        c = FF(c, d, a, b, M_offset_6, 17, T[6]);
        b = FF(b, c, d, a, M_offset_7, 22, T[7]);
        a = FF(a, b, c, d, M_offset_8, 7, T[8]);
        d = FF(d, a, b, c, M_offset_9, 12, T[9]);
        c = FF(c, d, a, b, M_offset_10, 17, T[10]);
        b = FF(b, c, d, a, M_offset_11, 22, T[11]);
        a = FF(a, b, c, d, M_offset_12, 7, T[12]);
        d = FF(d, a, b, c, M_offset_13, 12, T[13]);
        c = FF(c, d, a, b, M_offset_14, 17, T[14]);
        b = FF(b, c, d, a, M_offset_15, 22, T[15]);
        a = GG(a, b, c, d, M_offset_1, 5, T[16]);
        d = GG(d, a, b, c, M_offset_6, 9, T[17]);
        c = GG(c, d, a, b, M_offset_11, 14, T[18]);
        b = GG(b, c, d, a, M_offset_0, 20, T[19]);
        a = GG(a, b, c, d, M_offset_5, 5, T[20]);
        d = GG(d, a, b, c, M_offset_10, 9, T[21]);
        c = GG(c, d, a, b, M_offset_15, 14, T[22]);
        b = GG(b, c, d, a, M_offset_4, 20, T[23]);
        a = GG(a, b, c, d, M_offset_9, 5, T[24]);
        d = GG(d, a, b, c, M_offset_14, 9, T[25]);
        c = GG(c, d, a, b, M_offset_3, 14, T[26]);
        b = GG(b, c, d, a, M_offset_8, 20, T[27]);
        a = GG(a, b, c, d, M_offset_13, 5, T[28]);
        d = GG(d, a, b, c, M_offset_2, 9, T[29]);
        c = GG(c, d, a, b, M_offset_7, 14, T[30]);
        b = GG(b, c, d, a, M_offset_12, 20, T[31]);
        a = HH(a, b, c, d, M_offset_5, 4, T[32]);
        d = HH(d, a, b, c, M_offset_8, 11, T[33]);
        c = HH(c, d, a, b, M_offset_11, 16, T[34]);
        b = HH(b, c, d, a, M_offset_14, 23, T[35]);
        a = HH(a, b, c, d, M_offset_1, 4, T[36]);
        d = HH(d, a, b, c, M_offset_4, 11, T[37]);
        c = HH(c, d, a, b, M_offset_7, 16, T[38]);
        b = HH(b, c, d, a, M_offset_10, 23, T[39]);
        a = HH(a, b, c, d, M_offset_13, 4, T[40]);
        d = HH(d, a, b, c, M_offset_0, 11, T[41]);
        c = HH(c, d, a, b, M_offset_3, 16, T[42]);
        b = HH(b, c, d, a, M_offset_6, 23, T[43]);
        a = HH(a, b, c, d, M_offset_9, 4, T[44]);
        d = HH(d, a, b, c, M_offset_12, 11, T[45]);
        c = HH(c, d, a, b, M_offset_15, 16, T[46]);
        b = HH(b, c, d, a, M_offset_2, 23, T[47]);
        a = II(a, b, c, d, M_offset_0, 6, T[48]);
        d = II(d, a, b, c, M_offset_7, 10, T[49]);
        c = II(c, d, a, b, M_offset_14, 15, T[50]);
        b = II(b, c, d, a, M_offset_5, 21, T[51]);
        a = II(a, b, c, d, M_offset_12, 6, T[52]);
        d = II(d, a, b, c, M_offset_3, 10, T[53]);
        c = II(c, d, a, b, M_offset_10, 15, T[54]);
        b = II(b, c, d, a, M_offset_1, 21, T[55]);
        a = II(a, b, c, d, M_offset_8, 6, T[56]);
        d = II(d, a, b, c, M_offset_15, 10, T[57]);
        c = II(c, d, a, b, M_offset_6, 15, T[58]);
        b = II(b, c, d, a, M_offset_13, 21, T[59]);
        a = II(a, b, c, d, M_offset_4, 6, T[60]);
        d = II(d, a, b, c, M_offset_11, 10, T[61]);
        c = II(c, d, a, b, M_offset_2, 15, T[62]);
        b = II(b, c, d, a, M_offset_9, 21, T[63]);

        // Intermediate hash value
        H[0] = H[0] + a | 0;
        H[1] = H[1] + b | 0;
        H[2] = H[2] + c | 0;
        H[3] = H[3] + d | 0;
      }
      /* eslint-ensable no-param-reassign */

      _doFinalize() {
        // Shortcuts
        const data = this._data;
        const dataWords = data.words;
        const nBitsTotal = this._nDataBytes * 8;
        const nBitsLeft = data.sigBytes * 8;

        // Add padding
        dataWords[nBitsLeft >>> 5] |= 0x80 << 24 - nBitsLeft % 32;
        const nBitsTotalH = Math.floor(nBitsTotal / 0x100000000);
        const nBitsTotalL = nBitsTotal;
        dataWords[(nBitsLeft + 64 >>> 9 << 4) + 15] = (nBitsTotalH << 8 | nBitsTotalH >>> 24) & 0x00ff00ff | (nBitsTotalH << 24 | nBitsTotalH >>> 8) & 0xff00ff00;
        dataWords[(nBitsLeft + 64 >>> 9 << 4) + 14] = (nBitsTotalL << 8 | nBitsTotalL >>> 24) & 0x00ff00ff | (nBitsTotalL << 24 | nBitsTotalL >>> 8) & 0xff00ff00;
        data.sigBytes = (dataWords.length + 1) * 4;

        // Hash final blocks
        this._process();

        // Shortcuts
        const hash = this._hash;
        const H = hash.words;

        // Swap endian
        for (let i = 0; i < 4; i += 1) {
          // Shortcut
          const H_i = H[i];
          H[i] = (H_i << 8 | H_i >>> 24) & 0x00ff00ff | (H_i << 24 | H_i >>> 8) & 0xff00ff00;
        }

        // Return final computed hash
        return hash;
      }
      clone() {
        const clone = super.clone.call(this);
        clone._hash = this._hash.clone();
        return clone;
      }
    }

    /**
     * This key derivation function is meant to conform with EVP_BytesToKey.
     * www.openssl.org/docs/crypto/EVP_BytesToKey.html
     */
    class EvpKDFAlgo extends Base {
      /**
       * Initializes a newly created key derivation function.
       *
       * @param {Object} cfg (Optional) The configuration options to use for the derivation.
       *
       * @example
       *
       *     const kdf = CryptoJS.algo.EvpKDF.create();
       *     const kdf = CryptoJS.algo.EvpKDF.create({ keySize: 8 });
       *     const kdf = CryptoJS.algo.EvpKDF.create({ keySize: 8, iterations: 1000 });
       */
      constructor(cfg) {
        super();

        /**
         * Configuration options.
         *
         * @property {number} keySize The key size in words to generate. Default: 4 (128 bits)
         * @property {Hasher} hasher The hash algorithm to use. Default: MD5
         * @property {number} iterations The number of iterations to perform. Default: 1
         */
        this.cfg = Object.assign(new Base(), {
          keySize: 128 / 32,
          hasher: MD5Algo,
          iterations: 1
        }, cfg);
      }

      /**
       * Derives a key from a password.
       *
       * @param {WordArray|string} password The password.
       * @param {WordArray|string} salt A salt.
       *
       * @return {WordArray} The derived key.
       *
       * @example
       *
       *     const key = kdf.compute(password, salt);
       */
      compute(password, salt) {
        let block;

        // Shortcut
        const {
          cfg
        } = this;

        // Init hasher
        const hasher = cfg.hasher.create();

        // Initial values
        const derivedKey = WordArray.create();

        // Shortcuts
        const derivedKeyWords = derivedKey.words;
        const {
          keySize,
          iterations
        } = cfg;

        // Generate key
        while (derivedKeyWords.length < keySize) {
          if (block) {
            hasher.update(block);
          }
          block = hasher.update(password).finalize(salt);
          hasher.reset();

          // Iterations
          for (let i = 1; i < iterations; i += 1) {
            block = hasher.finalize(block);
            hasher.reset();
          }
          derivedKey.concat(block);
        }
        derivedKey.sigBytes = keySize * 4;
        return derivedKey;
      }
    }

    /* eslint-disable no-use-before-define */


    /**
     * Abstract base cipher template.
     *
     * @property {number} keySize This cipher's key size. Default: 4 (128 bits)
     * @property {number} ivSize This cipher's IV size. Default: 4 (128 bits)
     * @property {number} _ENC_XFORM_MODE A constant representing encryption mode.
     * @property {number} _DEC_XFORM_MODE A constant representing decryption mode.
     */
    class Cipher extends BufferedBlockAlgorithm {
      /**
       * Initializes a newly created cipher.
       *
       * @param {number} xformMode Either the encryption or decryption transormation mode constant.
       * @param {WordArray} key The key.
       * @param {Object} cfg (Optional) The configuration options to use for this operation.
       *
       * @example
       *
       *     const cipher = CryptoJS.algo.AES.create(
       *       CryptoJS.algo.AES._ENC_XFORM_MODE, keyWordArray, { iv: ivWordArray }
       *     );
       */
      constructor(xformMode, key, cfg) {
        super();

        /**
         * Configuration options.
         *
         * @property {WordArray} iv The IV to use for this operation.
         */
        this.cfg = Object.assign(new Base(), cfg);

        // Store transform mode and key
        this._xformMode = xformMode;
        this._key = key;

        // Set initial values
        this.reset();
      }

      /**
       * Creates this cipher in encryption mode.
       *
       * @param {WordArray} key The key.
       * @param {Object} cfg (Optional) The configuration options to use for this operation.
       *
       * @return {Cipher} A cipher instance.
       *
       * @static
       *
       * @example
       *
       *     const cipher = CryptoJS.algo.AES.createEncryptor(keyWordArray, { iv: ivWordArray });
       */
      static createEncryptor(key, cfg) {
        return this.create(this._ENC_XFORM_MODE, key, cfg);
      }

      /**
       * Creates this cipher in decryption mode.
       *
       * @param {WordArray} key The key.
       * @param {Object} cfg (Optional) The configuration options to use for this operation.
       *
       * @return {Cipher} A cipher instance.
       *
       * @static
       *
       * @example
       *
       *     const cipher = CryptoJS.algo.AES.createDecryptor(keyWordArray, { iv: ivWordArray });
       */
      static createDecryptor(key, cfg) {
        return this.create(this._DEC_XFORM_MODE, key, cfg);
      }

      /**
       * Creates shortcut functions to a cipher's object interface.
       *
       * @param {Cipher} cipher The cipher to create a helper for.
       *
       * @return {Object} An object with encrypt and decrypt shortcut functions.
       *
       * @static
       *
       * @example
       *
       *     const AES = CryptoJS.lib.Cipher._createHelper(CryptoJS.algo.AES);
       */
      static _createHelper(SubCipher) {
        const selectCipherStrategy = key => {
          if (typeof key === 'string') {
            return PasswordBasedCipher;
          }
          return SerializableCipher;
        };
        return {
          encrypt(message, key, cfg) {
            return selectCipherStrategy(key).encrypt(SubCipher, message, key, cfg);
          },
          decrypt(ciphertext, key, cfg) {
            return selectCipherStrategy(key).decrypt(SubCipher, ciphertext, key, cfg);
          }
        };
      }

      /**
       * Resets this cipher to its initial state.
       *
       * @example
       *
       *     cipher.reset();
       */
      reset() {
        // Reset data buffer
        super.reset.call(this);

        // Perform concrete-cipher logic
        this._doReset();
      }

      /**
       * Adds data to be encrypted or decrypted.
       *
       * @param {WordArray|string} dataUpdate The data to encrypt or decrypt.
       *
       * @return {WordArray} The data after processing.
       *
       * @example
       *
       *     const encrypted = cipher.process('data');
       *     const encrypted = cipher.process(wordArray);
       */
      process(dataUpdate) {
        // Append
        this._append(dataUpdate);

        // Process available blocks
        return this._process();
      }

      /**
       * Finalizes the encryption or decryption process.
       * Note that the finalize operation is effectively a destructive, read-once operation.
       *
       * @param {WordArray|string} dataUpdate The final data to encrypt or decrypt.
       *
       * @return {WordArray} The data after final processing.
       *
       * @example
       *
       *     const encrypted = cipher.finalize();
       *     const encrypted = cipher.finalize('data');
       *     const encrypted = cipher.finalize(wordArray);
       */
      finalize(dataUpdate) {
        // Final data update
        if (dataUpdate) {
          this._append(dataUpdate);
        }

        // Perform concrete-cipher logic
        const finalProcessedData = this._doFinalize();
        return finalProcessedData;
      }
    }
    Cipher._ENC_XFORM_MODE = 1;
    Cipher._DEC_XFORM_MODE = 2;
    Cipher.keySize = 128 / 32;
    Cipher.ivSize = 128 / 32;

    /**
     * Abstract base block cipher mode template.
     */
    class BlockCipherMode extends Base {
      /**
       * Initializes a newly created mode.
       *
       * @param {Cipher} cipher A block cipher instance.
       * @param {Array} iv The IV words.
       *
       * @example
       *
       *     const mode = CryptoJS.mode.CBC.Encryptor.create(cipher, iv.words);
       */
      constructor(cipher, iv) {
        super();
        this._cipher = cipher;
        this._iv = iv;
      }

      /**
       * Creates this mode for encryption.
       *
       * @param {Cipher} cipher A block cipher instance.
       * @param {Array} iv The IV words.
       *
       * @static
       *
       * @example
       *
       *     const mode = CryptoJS.mode.CBC.createEncryptor(cipher, iv.words);
       */
      static createEncryptor(cipher, iv) {
        return this.Encryptor.create(cipher, iv);
      }

      /**
       * Creates this mode for decryption.
       *
       * @param {Cipher} cipher A block cipher instance.
       * @param {Array} iv The IV words.
       *
       * @static
       *
       * @example
       *
       *     const mode = CryptoJS.mode.CBC.createDecryptor(cipher, iv.words);
       */
      static createDecryptor(cipher, iv) {
        return this.Decryptor.create(cipher, iv);
      }
    }
    function xorBlock(words, offset, blockSize) {
      const _words = words;
      let block;

      // Shortcut
      const iv = this._iv;

      // Choose mixing block
      if (iv) {
        block = iv;

        // Remove IV for subsequent blocks
        this._iv = undefined;
      } else {
        block = this._prevBlock;
      }

      // XOR blocks
      for (let i = 0; i < blockSize; i += 1) {
        _words[offset + i] ^= block[i];
      }
    }

    /**
     * Cipher Block Chaining mode.
     */

    /**
     * Abstract base CBC mode.
     */
    class CBC extends BlockCipherMode {}
    /**
     * CBC encryptor.
     */
    CBC.Encryptor = class extends CBC {
      /**
       * Processes the data block at offset.
       *
       * @param {Array} words The data words to operate on.
       * @param {number} offset The offset where the block starts.
       *
       * @example
       *
       *     mode.processBlock(data.words, offset);
       */
      processBlock(words, offset) {
        // Shortcuts
        const cipher = this._cipher;
        const {
          blockSize
        } = cipher;

        // XOR and encrypt
        xorBlock.call(this, words, offset, blockSize);
        cipher.encryptBlock(words, offset);

        // Remember this block to use with next block
        this._prevBlock = words.slice(offset, offset + blockSize);
      }
    };
    /**
     * CBC decryptor.
     */
    CBC.Decryptor = class extends CBC {
      /**
       * Processes the data block at offset.
       *
       * @param {Array} words The data words to operate on.
       * @param {number} offset The offset where the block starts.
       *
       * @example
       *
       *     mode.processBlock(data.words, offset);
       */
      processBlock(words, offset) {
        // Shortcuts
        const cipher = this._cipher;
        const {
          blockSize
        } = cipher;

        // Remember this block to use with next block
        const thisBlock = words.slice(offset, offset + blockSize);

        // Decrypt and XOR
        cipher.decryptBlock(words, offset);
        xorBlock.call(this, words, offset, blockSize);

        // This block becomes the previous block
        this._prevBlock = thisBlock;
      }
    };

    /**
     * PKCS #5/7 padding strategy.
     */
    const Pkcs7 = {
      /**
       * Pads data using the algorithm defined in PKCS #5/7.
       *
       * @param {WordArray} data The data to pad.
       * @param {number} blockSize The multiple that the data should be padded to.
       *
       * @static
       *
       * @example
       *
       *     CryptoJS.pad.Pkcs7.pad(wordArray, 4);
       */
      pad(data, blockSize) {
        // Shortcut
        const blockSizeBytes = blockSize * 4;

        // Count padding bytes
        const nPaddingBytes = blockSizeBytes - data.sigBytes % blockSizeBytes;

        // Create padding word
        const paddingWord = nPaddingBytes << 24 | nPaddingBytes << 16 | nPaddingBytes << 8 | nPaddingBytes;

        // Create padding
        const paddingWords = [];
        for (let i = 0; i < nPaddingBytes; i += 4) {
          paddingWords.push(paddingWord);
        }
        const padding = WordArray.create(paddingWords, nPaddingBytes);

        // Add padding
        data.concat(padding);
      },
      /**
       * Unpads data that had been padded using the algorithm defined in PKCS #5/7.
       *
       * @param {WordArray} data The data to unpad.
       *
       * @static
       *
       * @example
       *
       *     CryptoJS.pad.Pkcs7.unpad(wordArray);
       */
      unpad(data) {
        const _data = data;

        // Get number of padding bytes from last byte
        const nPaddingBytes = _data.words[_data.sigBytes - 1 >>> 2] & 0xff;

        // Remove padding
        _data.sigBytes -= nPaddingBytes;
      }
    };

    /**
     * Abstract base block cipher template.
     *
     * @property {number} blockSize
     *
     *    The number of 32-bit words this cipher operates on. Default: 4 (128 bits)
     */
    class BlockCipher extends Cipher {
      constructor(xformMode, key, cfg) {
        /**
         * Configuration options.
         *
         * @property {Mode} mode The block mode to use. Default: CBC
         * @property {Padding} padding The padding strategy to use. Default: Pkcs7
         */
        super(xformMode, key, Object.assign({
          mode: CBC,
          padding: Pkcs7
        }, cfg));
        this.blockSize = 128 / 32;
      }
      reset() {
        let modeCreator;

        // Reset cipher
        super.reset.call(this);

        // Shortcuts
        const {
          cfg
        } = this;
        const {
          iv,
          mode
        } = cfg;

        // Reset block mode
        if (this._xformMode === this.constructor._ENC_XFORM_MODE) {
          modeCreator = mode.createEncryptor;
        } else /* if (this._xformMode == this._DEC_XFORM_MODE) */{
            modeCreator = mode.createDecryptor;
            // Keep at least one block in the buffer for unpadding
            this._minBufferSize = 1;
          }
        this._mode = modeCreator.call(mode, this, iv && iv.words);
        this._mode.__creator = modeCreator;
      }
      _doProcessBlock(words, offset) {
        this._mode.processBlock(words, offset);
      }
      _doFinalize() {
        let finalProcessedBlocks;

        // Shortcut
        const {
          padding
        } = this.cfg;

        // Finalize
        if (this._xformMode === this.constructor._ENC_XFORM_MODE) {
          // Pad data
          padding.pad(this._data, this.blockSize);

          // Process final blocks
          finalProcessedBlocks = this._process(!!'flush');
        } else /* if (this._xformMode == this._DEC_XFORM_MODE) */{
            // Process final blocks
            finalProcessedBlocks = this._process(!!'flush');

            // Unpad data
            padding.unpad(finalProcessedBlocks);
          }
        return finalProcessedBlocks;
      }
    }

    /**
     * A collection of cipher parameters.
     *
     * @property {WordArray} ciphertext The raw ciphertext.
     * @property {WordArray} key The key to this ciphertext.
     * @property {WordArray} iv The IV used in the ciphering operation.
     * @property {WordArray} salt The salt used with a key derivation function.
     * @property {Cipher} algorithm The cipher algorithm.
     * @property {Mode} mode The block mode used in the ciphering operation.
     * @property {Padding} padding The padding scheme used in the ciphering operation.
     * @property {number} blockSize The block size of the cipher.
     * @property {Format} formatter
     *    The default formatting strategy to convert this cipher params object to a string.
     */
    class CipherParams extends Base {
      /**
       * Initializes a newly created cipher params object.
       *
       * @param {Object} cipherParams An object with any of the possible cipher parameters.
       *
       * @example
       *
       *     var cipherParams = CryptoJS.lib.CipherParams.create({
       *         ciphertext: ciphertextWordArray,
       *         key: keyWordArray,
       *         iv: ivWordArray,
       *         salt: saltWordArray,
       *         algorithm: CryptoJS.algo.AES,
       *         mode: CryptoJS.mode.CBC,
       *         padding: CryptoJS.pad.PKCS7,
       *         blockSize: 4,
       *         formatter: CryptoJS.format.OpenSSL
       *     });
       */
      constructor(cipherParams) {
        super();
        this.mixIn(cipherParams);
      }

      /**
       * Converts this cipher params object to a string.
       *
       * @param {Format} formatter (Optional) The formatting strategy to use.
       *
       * @return {string} The stringified cipher params.
       *
       * @throws Error If neither the formatter nor the default formatter is set.
       *
       * @example
       *
       *     var string = cipherParams + '';
       *     var string = cipherParams.toString();
       *     var string = cipherParams.toString(CryptoJS.format.OpenSSL);
       */
      toString(formatter) {
        return (formatter || this.formatter).stringify(this);
      }
    }

    /**
     * OpenSSL formatting strategy.
     */
    const OpenSSLFormatter = {
      /**
       * Converts a cipher params object to an OpenSSL-compatible string.
       *
       * @param {CipherParams} cipherParams The cipher params object.
       *
       * @return {string} The OpenSSL-compatible string.
       *
       * @static
       *
       * @example
       *
       *     var openSSLString = CryptoJS.format.OpenSSL.stringify(cipherParams);
       */
      stringify(cipherParams) {
        let wordArray;

        // Shortcuts
        const {
          ciphertext,
          salt
        } = cipherParams;

        // Format
        if (salt) {
          wordArray = WordArray.create([0x53616c74, 0x65645f5f]).concat(salt).concat(ciphertext);
        } else {
          wordArray = ciphertext;
        }
        return wordArray.toString(Base64);
      },
      /**
       * Converts an OpenSSL-compatible string to a cipher params object.
       *
       * @param {string} openSSLStr The OpenSSL-compatible string.
       *
       * @return {CipherParams} The cipher params object.
       *
       * @static
       *
       * @example
       *
       *     var cipherParams = CryptoJS.format.OpenSSL.parse(openSSLString);
       */
      parse(openSSLStr) {
        let salt;

        // Parse base64
        const ciphertext = Base64.parse(openSSLStr);

        // Shortcut
        const ciphertextWords = ciphertext.words;

        // Test for salt
        if (ciphertextWords[0] === 0x53616c74 && ciphertextWords[1] === 0x65645f5f) {
          // Extract salt
          salt = WordArray.create(ciphertextWords.slice(2, 4));

          // Remove salt from ciphertext
          ciphertextWords.splice(0, 4);
          ciphertext.sigBytes -= 16;
        }
        return CipherParams.create({
          ciphertext,
          salt
        });
      }
    };

    /**
     * A cipher wrapper that returns ciphertext as a serializable cipher params object.
     */
    class SerializableCipher extends Base {
      /**
       * Encrypts a message.
       *
       * @param {Cipher} cipher The cipher algorithm to use.
       * @param {WordArray|string} message The message to encrypt.
       * @param {WordArray} key The key.
       * @param {Object} cfg (Optional) The configuration options to use for this operation.
       *
       * @return {CipherParams} A cipher params object.
       *
       * @static
       *
       * @example
       *
       *     var ciphertextParams = CryptoJS.lib.SerializableCipher
       *       .encrypt(CryptoJS.algo.AES, message, key);
       *     var ciphertextParams = CryptoJS.lib.SerializableCipher
       *       .encrypt(CryptoJS.algo.AES, message, key, { iv: iv });
       *     var ciphertextParams = CryptoJS.lib.SerializableCipher
       *       .encrypt(CryptoJS.algo.AES, message, key, { iv: iv, format: CryptoJS.format.OpenSSL });
       */
      static encrypt(cipher, message, key, cfg) {
        // Apply config defaults
        const _cfg = Object.assign(new Base(), this.cfg, cfg);

        // Encrypt
        const encryptor = cipher.createEncryptor(key, _cfg);
        const ciphertext = encryptor.finalize(message);

        // Shortcut
        const cipherCfg = encryptor.cfg;

        // Create and return serializable cipher params
        return CipherParams.create({
          ciphertext,
          key,
          iv: cipherCfg.iv,
          algorithm: cipher,
          mode: cipherCfg.mode,
          padding: cipherCfg.padding,
          blockSize: encryptor.blockSize,
          formatter: _cfg.format
        });
      }

      /**
       * Decrypts serialized ciphertext.
       *
       * @param {Cipher} cipher The cipher algorithm to use.
       * @param {CipherParams|string} ciphertext The ciphertext to decrypt.
       * @param {WordArray} key The key.
       * @param {Object} cfg (Optional) The configuration options to use for this operation.
       *
       * @return {WordArray} The plaintext.
       *
       * @static
       *
       * @example
       *
       *     var plaintext = CryptoJS.lib.SerializableCipher
       *       .decrypt(CryptoJS.algo.AES, formattedCiphertext, key,
       *         { iv: iv, format: CryptoJS.format.OpenSSL });
       *     var plaintext = CryptoJS.lib.SerializableCipher
       *       .decrypt(CryptoJS.algo.AES, ciphertextParams, key,
       *         { iv: iv, format: CryptoJS.format.OpenSSL });
       */
      static decrypt(cipher, ciphertext, key, cfg) {
        let _ciphertext = ciphertext;

        // Apply config defaults
        const _cfg = Object.assign(new Base(), this.cfg, cfg);

        // Convert string to CipherParams
        _ciphertext = this._parse(_ciphertext, _cfg.format);

        // Decrypt
        const plaintext = cipher.createDecryptor(key, _cfg).finalize(_ciphertext.ciphertext);
        return plaintext;
      }

      /**
       * Converts serialized ciphertext to CipherParams,
       * else assumed CipherParams already and returns ciphertext unchanged.
       *
       * @param {CipherParams|string} ciphertext The ciphertext.
       * @param {Formatter} format The formatting strategy to use to parse serialized ciphertext.
       *
       * @return {CipherParams} The unserialized ciphertext.
       *
       * @static
       *
       * @example
       *
       *     var ciphertextParams = CryptoJS.lib.SerializableCipher
       *       ._parse(ciphertextStringOrParams, format);
       */
      static _parse(ciphertext, format) {
        if (typeof ciphertext === 'string') {
          return format.parse(ciphertext, this);
        }
        return ciphertext;
      }
    }
    /**
     * Configuration options.
     *
     * @property {Formatter} format
     *
     *    The formatting strategy to convert cipher param objects to and from a string.
     *    Default: OpenSSL
     */
    SerializableCipher.cfg = Object.assign(new Base(), {
      format: OpenSSLFormatter
    });

    /**
     * OpenSSL key derivation function.
     */
    const OpenSSLKdf = {
      /**
       * Derives a key and IV from a password.
       *
       * @param {string} password The password to derive from.
       * @param {number} keySize The size in words of the key to generate.
       * @param {number} ivSize The size in words of the IV to generate.
       * @param {WordArray|string} salt
       *     (Optional) A 64-bit salt to use. If omitted, a salt will be generated randomly.
       *
       * @return {CipherParams} A cipher params object with the key, IV, and salt.
       *
       * @static
       *
       * @example
       *
       *     var derivedParams = CryptoJS.kdf.OpenSSL.execute('Password', 256/32, 128/32);
       *     var derivedParams = CryptoJS.kdf.OpenSSL.execute('Password', 256/32, 128/32, 'saltsalt');
       */
      execute(password, keySize, ivSize, salt, hasher) {
        let _salt = salt;

        // Generate random salt
        if (!_salt) {
          _salt = WordArray.random(64 / 8);
        }

        // Derive key and IV
        let key;
        if (!hasher) {
          key = EvpKDFAlgo.create({
            keySize: keySize + ivSize
          }).compute(password, _salt);
        } else {
          key = EvpKDFAlgo.create({
            keySize: keySize + ivSize,
            hasher
          }).compute(password, _salt);
        }

        // Separate key and IV
        const iv = WordArray.create(key.words.slice(keySize), ivSize * 4);
        key.sigBytes = keySize * 4;

        // Return params
        return CipherParams.create({
          key,
          iv,
          salt: _salt
        });
      }
    };

    /**
     * A serializable cipher wrapper that derives the key from a password,
     * and returns ciphertext as a serializable cipher params object.
     */
    class PasswordBasedCipher extends SerializableCipher {
      /**
       * Encrypts a message using a password.
       *
       * @param {Cipher} cipher The cipher algorithm to use.
       * @param {WordArray|string} message The message to encrypt.
       * @param {string} password The password.
       * @param {Object} cfg (Optional) The configuration options to use for this operation.
       *
       * @return {CipherParams} A cipher params object.
       *
       * @static
       *
       * @example
       *
       *     var ciphertextParams = CryptoJS.lib.PasswordBasedCipher
       *       .encrypt(CryptoJS.algo.AES, message, 'password');
       *     var ciphertextParams = CryptoJS.lib.PasswordBasedCipher
       *       .encrypt(CryptoJS.algo.AES, message, 'password', { format: CryptoJS.format.OpenSSL });
       */
      static encrypt(cipher, message, password, cfg) {
        // Apply config defaults
        const _cfg = Object.assign(new Base(), this.cfg, cfg);

        // Derive key and other params
        const derivedParams = _cfg.kdf.execute(password, cipher.keySize, cipher.ivSize, _cfg.salt, _cfg.hasher);

        // Add IV to config
        _cfg.iv = derivedParams.iv;

        // Encrypt
        const ciphertext = SerializableCipher.encrypt.call(this, cipher, message, derivedParams.key, _cfg);

        // Mix in derived params
        ciphertext.mixIn(derivedParams);
        return ciphertext;
      }

      /**
       * Decrypts serialized ciphertext using a password.
       *
       * @param {Cipher} cipher The cipher algorithm to use.
       * @param {CipherParams|string} ciphertext The ciphertext to decrypt.
       * @param {string} password The password.
       * @param {Object} cfg (Optional) The configuration options to use for this operation.
       *
       * @return {WordArray} The plaintext.
       *
       * @static
       *
       * @example
       *
       *     var plaintext = CryptoJS.lib.PasswordBasedCipher
       *       .decrypt(CryptoJS.algo.AES, formattedCiphertext, 'password',
       *         { format: CryptoJS.format.OpenSSL });
       *     var plaintext = CryptoJS.lib.PasswordBasedCipher
       *       .decrypt(CryptoJS.algo.AES, ciphertextParams, 'password',
       *         { format: CryptoJS.format.OpenSSL });
       */
      static decrypt(cipher, ciphertext, password, cfg) {
        let _ciphertext = ciphertext;

        // Apply config defaults
        const _cfg = Object.assign(new Base(), this.cfg, cfg);

        // Convert string to CipherParams
        _ciphertext = this._parse(_ciphertext, _cfg.format);

        // Derive key and other params
        const derivedParams = _cfg.kdf.execute(password, cipher.keySize, cipher.ivSize, _ciphertext.salt, _cfg.hasher);

        // Add IV to config
        _cfg.iv = derivedParams.iv;

        // Decrypt
        const plaintext = SerializableCipher.decrypt.call(this, cipher, _ciphertext, derivedParams.key, _cfg);
        return plaintext;
      }
    }
    /**
     * Configuration options.
     *
     * @property {KDF} kdf
     *     The key derivation function to use to generate a key and IV from a password.
     *     Default: OpenSSL
     */
    PasswordBasedCipher.cfg = Object.assign(SerializableCipher.cfg, {
      kdf: OpenSSLKdf
    });

    // Lookup tables
    const _SBOX = [];
    const INV_SBOX = [];
    const _SUB_MIX_0 = [];
    const _SUB_MIX_1 = [];
    const _SUB_MIX_2 = [];
    const _SUB_MIX_3 = [];
    const INV_SUB_MIX_0 = [];
    const INV_SUB_MIX_1 = [];
    const INV_SUB_MIX_2 = [];
    const INV_SUB_MIX_3 = [];

    // Compute lookup tables

    // Compute double table
    const d = [];
    for (let i = 0; i < 256; i += 1) {
      if (i < 128) {
        d[i] = i << 1;
      } else {
        d[i] = i << 1 ^ 0x11b;
      }
    }

    // Walk GF(2^8)
    let x = 0;
    let xi = 0;
    for (let i = 0; i < 256; i += 1) {
      // Compute sbox
      let sx = xi ^ xi << 1 ^ xi << 2 ^ xi << 3 ^ xi << 4;
      sx = sx >>> 8 ^ sx & 0xff ^ 0x63;
      _SBOX[x] = sx;
      INV_SBOX[sx] = x;

      // Compute multiplication
      const x2 = d[x];
      const x4 = d[x2];
      const x8 = d[x4];

      // Compute sub bytes, mix columns tables
      let t = d[sx] * 0x101 ^ sx * 0x1010100;
      _SUB_MIX_0[x] = t << 24 | t >>> 8;
      _SUB_MIX_1[x] = t << 16 | t >>> 16;
      _SUB_MIX_2[x] = t << 8 | t >>> 24;
      _SUB_MIX_3[x] = t;

      // Compute inv sub bytes, inv mix columns tables
      t = x8 * 0x1010101 ^ x4 * 0x10001 ^ x2 * 0x101 ^ x * 0x1010100;
      INV_SUB_MIX_0[sx] = t << 24 | t >>> 8;
      INV_SUB_MIX_1[sx] = t << 16 | t >>> 16;
      INV_SUB_MIX_2[sx] = t << 8 | t >>> 24;
      INV_SUB_MIX_3[sx] = t;

      // Compute next counter
      if (!x) {
        xi = 1;
        x = xi;
      } else {
        x = x2 ^ d[d[d[x8 ^ x2]]];
        xi ^= d[d[xi]];
      }
    }

    // Precomputed Rcon lookup
    const RCON = [0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36];

    /**
     * AES block cipher algorithm.
     */
    class AESAlgo extends BlockCipher {
      _doReset() {
        let t;

        // Skip reset of nRounds has been set before and key did not change
        if (this._nRounds && this._keyPriorReset === this._key) {
          return;
        }

        // Shortcuts
        this._keyPriorReset = this._key;
        const key = this._keyPriorReset;
        const keyWords = key.words;
        const keySize = key.sigBytes / 4;

        // Compute number of rounds
        this._nRounds = keySize + 6;
        const nRounds = this._nRounds;

        // Compute number of key schedule rows
        const ksRows = (nRounds + 1) * 4;

        // Compute key schedule
        this._keySchedule = [];
        const keySchedule = this._keySchedule;
        for (let ksRow = 0; ksRow < ksRows; ksRow += 1) {
          if (ksRow < keySize) {
            keySchedule[ksRow] = keyWords[ksRow];
          } else {
            t = keySchedule[ksRow - 1];
            if (!(ksRow % keySize)) {
              // Rot word
              t = t << 8 | t >>> 24;

              // Sub word
              t = _SBOX[t >>> 24] << 24 | _SBOX[t >>> 16 & 0xff] << 16 | _SBOX[t >>> 8 & 0xff] << 8 | _SBOX[t & 0xff];

              // Mix Rcon
              t ^= RCON[ksRow / keySize | 0] << 24;
            } else if (keySize > 6 && ksRow % keySize === 4) {
              // Sub word
              t = _SBOX[t >>> 24] << 24 | _SBOX[t >>> 16 & 0xff] << 16 | _SBOX[t >>> 8 & 0xff] << 8 | _SBOX[t & 0xff];
            }
            keySchedule[ksRow] = keySchedule[ksRow - keySize] ^ t;
          }
        }

        // Compute inv key schedule
        this._invKeySchedule = [];
        const invKeySchedule = this._invKeySchedule;
        for (let invKsRow = 0; invKsRow < ksRows; invKsRow += 1) {
          const ksRow = ksRows - invKsRow;
          if (invKsRow % 4) {
            t = keySchedule[ksRow];
          } else {
            t = keySchedule[ksRow - 4];
          }
          if (invKsRow < 4 || ksRow <= 4) {
            invKeySchedule[invKsRow] = t;
          } else {
            invKeySchedule[invKsRow] = INV_SUB_MIX_0[_SBOX[t >>> 24]] ^ INV_SUB_MIX_1[_SBOX[t >>> 16 & 0xff]] ^ INV_SUB_MIX_2[_SBOX[t >>> 8 & 0xff]] ^ INV_SUB_MIX_3[_SBOX[t & 0xff]];
          }
        }
      }
      encryptBlock(M, offset) {
        this._doCryptBlock(M, offset, this._keySchedule, _SUB_MIX_0, _SUB_MIX_1, _SUB_MIX_2, _SUB_MIX_3, _SBOX);
      }
      decryptBlock(M, offset) {
        const _M = M;

        // Swap 2nd and 4th rows
        let t = _M[offset + 1];
        _M[offset + 1] = _M[offset + 3];
        _M[offset + 3] = t;
        this._doCryptBlock(_M, offset, this._invKeySchedule, INV_SUB_MIX_0, INV_SUB_MIX_1, INV_SUB_MIX_2, INV_SUB_MIX_3, INV_SBOX);

        // Inv swap 2nd and 4th rows
        t = _M[offset + 1];
        _M[offset + 1] = _M[offset + 3];
        _M[offset + 3] = t;
      }
      _doCryptBlock(M, offset, keySchedule, SUB_MIX_0, SUB_MIX_1, SUB_MIX_2, SUB_MIX_3, SBOX) {
        const _M = M;

        // Shortcut
        const nRounds = this._nRounds;

        // Get input, add round key
        let s0 = _M[offset] ^ keySchedule[0];
        let s1 = _M[offset + 1] ^ keySchedule[1];
        let s2 = _M[offset + 2] ^ keySchedule[2];
        let s3 = _M[offset + 3] ^ keySchedule[3];

        // Key schedule row counter
        let ksRow = 4;

        // Rounds
        for (let round = 1; round < nRounds; round += 1) {
          // Shift rows, sub bytes, mix columns, add round key
          const t0 = SUB_MIX_0[s0 >>> 24] ^ SUB_MIX_1[s1 >>> 16 & 0xff] ^ SUB_MIX_2[s2 >>> 8 & 0xff] ^ SUB_MIX_3[s3 & 0xff] ^ keySchedule[ksRow];
          ksRow += 1;
          const t1 = SUB_MIX_0[s1 >>> 24] ^ SUB_MIX_1[s2 >>> 16 & 0xff] ^ SUB_MIX_2[s3 >>> 8 & 0xff] ^ SUB_MIX_3[s0 & 0xff] ^ keySchedule[ksRow];
          ksRow += 1;
          const t2 = SUB_MIX_0[s2 >>> 24] ^ SUB_MIX_1[s3 >>> 16 & 0xff] ^ SUB_MIX_2[s0 >>> 8 & 0xff] ^ SUB_MIX_3[s1 & 0xff] ^ keySchedule[ksRow];
          ksRow += 1;
          const t3 = SUB_MIX_0[s3 >>> 24] ^ SUB_MIX_1[s0 >>> 16 & 0xff] ^ SUB_MIX_2[s1 >>> 8 & 0xff] ^ SUB_MIX_3[s2 & 0xff] ^ keySchedule[ksRow];
          ksRow += 1;

          // Update state
          s0 = t0;
          s1 = t1;
          s2 = t2;
          s3 = t3;
        }

        // Shift rows, sub bytes, add round key
        const t0 = (SBOX[s0 >>> 24] << 24 | SBOX[s1 >>> 16 & 0xff] << 16 | SBOX[s2 >>> 8 & 0xff] << 8 | SBOX[s3 & 0xff]) ^ keySchedule[ksRow];
        ksRow += 1;
        const t1 = (SBOX[s1 >>> 24] << 24 | SBOX[s2 >>> 16 & 0xff] << 16 | SBOX[s3 >>> 8 & 0xff] << 8 | SBOX[s0 & 0xff]) ^ keySchedule[ksRow];
        ksRow += 1;
        const t2 = (SBOX[s2 >>> 24] << 24 | SBOX[s3 >>> 16 & 0xff] << 16 | SBOX[s0 >>> 8 & 0xff] << 8 | SBOX[s1 & 0xff]) ^ keySchedule[ksRow];
        ksRow += 1;
        const t3 = (SBOX[s3 >>> 24] << 24 | SBOX[s0 >>> 16 & 0xff] << 16 | SBOX[s1 >>> 8 & 0xff] << 8 | SBOX[s2 & 0xff]) ^ keySchedule[ksRow];
        ksRow += 1;

        // Set output
        _M[offset] = t0;
        _M[offset + 1] = t1;
        _M[offset + 2] = t2;
        _M[offset + 3] = t3;
      }
    }
    AESAlgo.keySize = 256 / 32;

    /**
     * Shortcut functions to the cipher's object interface.
     *
     * @example
     *
     *     var ciphertext = CryptoJS.AES.encrypt(message, key, cfg);
     *     var plaintext  = CryptoJS.AES.decrypt(ciphertext, key, cfg);
     */
    const AES = BlockCipher._createHelper(AESAlgo);

    var EncryptDog = /** @class */ (function () {
        function EncryptDog(key) {
            this.key = Utf8.parse('AvnlIOSDvasdfeaoiukjdsar');
            if (key) {
                this.key = Utf8.parse(key);
            }
        }
        EncryptDog.prototype.encrypt = function (str, ivstr) {
            var iv = ivstr ? Hex.parse(ivstr) : WordArray.random(16);
            var srcs = Utf8.parse(str);
            var encrypted = AES.encrypt(srcs, this.key, {
                iv: iv,
                mode: CBC,
                padding: Pkcs7
            });
            return encrypted.ciphertext.toString().toUpperCase() + ":" + iv.toString(Hex);
        };
        EncryptDog.prototype.decrypt = function (str) {
            var _a = str.split(':'), ciphertext = _a[0], ivstr = _a[1];
            var iv = Hex.parse(ivstr);
            var decrypted = AES.decrypt({ ciphertext: Hex.parse(ciphertext) }, this.key, { iv: iv, mode: CBC, padding: Pkcs7 });
            return decrypted.toString(Utf8);
        };
        return EncryptDog;
    }());

    var cookieKey = 'goN9uW4i0iKzP';
    var serverCookie = 'goN9uW4i0iKzO';
    // window.addEventListener('load',init)
    init();
    function init() {
        return __awaiter(this, void 0, void 0, function () {
            var cookeieEncryptKey, iscooke, cookieEncrypt, cookieValue, _a, _b, _c, _i, botKey, s, plugininfo, newTestBotString, _d, iv, oldcookie;
            return __generator(this, function (_e) {
                switch (_e.label) {
                    case 0:
                        cookeieEncryptKey = getCookie(serverCookie);
                        iscooke = getCookie(cookieKey);
                        cookieEncrypt = new EncryptDog(cookeieEncryptKey.substring(0, 32));
                        cookieValue = [];
                        _a = hasBot;
                        _b = [];
                        for (_c in _a)
                            _b.push(_c);
                        _i = 0;
                        _e.label = 1;
                    case 1:
                        if (!(_i < _b.length)) return [3 /*break*/, 4];
                        _c = _b[_i];
                        if (!(_c in _a)) return [3 /*break*/, 3];
                        botKey = _c;
                        return [4 /*yield*/, hasBot[botKey]()];
                    case 2:
                        s = _e.sent();
                        cookieValue.push(s);
                        _e.label = 3;
                    case 3:
                        _i++;
                        return [3 /*break*/, 1];
                    case 4: return [4 /*yield*/, pluginCheck()];
                    case 5:
                        plugininfo = _e.sent();
                        plugininfo.forEach(function (n) {
                            cookieValue.push(n.status === 'rejected' ? 0 : 1);
                        });
                        newTestBotString = cookieEncrypt.encrypt(cookieValue.join(','));
                        if (!!iscooke) {
                            _d = iscooke.split(':'), _d[0], iv = _d[1];
                            oldcookie = cookieEncrypt.encrypt(cookieValue.join(','), iv);
                            if (oldcookie === iscooke) {
                                return [2 /*return*/];
                            }
                        }
                        setCookie(cookieKey, newTestBotString);
                        // if(!document.referrer){
                        // }
                        location.href = location.href;
                        return [2 /*return*/];
                }
            });
        });
    }

})();

            
            
        </script>
    </body>
</html>
"""

app = FastAPI()

@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/api/web_socket")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")


# @app.websocket("/websocket/test01")
# def web_socket_test01(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_text()
#         await websocket.send_text(f"Message text was: {data}")


if __name__ == '__main__':
    uvicorn.run("web_socket_wss:app", reload=True, host="0.0.0.0", port=1025, ssl_keyfile="0.0.0.0-key.pem",
                ssl_certfile="0.0.0.0.pem")
