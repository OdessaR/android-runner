'use strict';

define(['lodash/dist/lodash', 'bam.cookies/cookies'], function(_, cookies) {

    /**
     *
     * @desc This is just a helper to encode the custom params.
     * @param {object} params
     *
     */
    function encodeCustomParams(params) {
        var encodedParams = '';

        for (var key in params) {
            if (params.hasOwnProperty(key)) {
                encodedParams = encodedParams + key + '%3D' + params[key] + '%26';
            }
        }

        return encodedParams.substring(0, encodedParams.length - 3);
    }

    /**
     *
     * @desc Function to override the default `DfpRequestBuilder.build(config, mediaItem, cuePoint)`
     * The override is passed 3 arguments:
     * 1. config The ad config object. The current ad provider is DFP.
     * 2. mediaItem The MediaItem/clip object
     * 3. cuePointVO  CuePoint object representing ID3 queue point
     * metadata. Currently only used on live events (mlb.tv).
     *
     */
    function customAdRequestBuilder(config, clip) {
        // Attempt to get 'url' from the adConfig, then from 'config', defaulting to hardcoded value
        const url = _.get(config, 'url', 'https://pubads.g.doubleclick.net/gampad/ads');
        const playerWidth = _.get(config, 'width');
        const playerHeight = _.get(config, 'height');
        const custParams = _.get(config, 'cust_params', {});
        const contentId = _.get(clip, 'contentId');
        const topicId = _.get(config, 'customPlayerParams.topicId', '');

        // THe DfpPlugin will set the player width and height on the dfp config for you to use here

        custParams.aam_uuid = cookies.get('aam_uuid') || '';

        if (contentId) {
            custParams.vid = contentId;
        }

        if (env) {
            custParams.env = env;
        }

        if (playerWidth) {
            custParams.width = playerWidth;
        }

        if (playerHeight) {
            custParams.height = playerHeight;
        }

        if (topicId) {
            custParams.topic = topicId;
        }

        let mapper = {

            autoplay: _.get(config, 'autoPlay'),
            output: _.get(config, 'output', 'vmap'),
            description_url: _.get(config, 'description_url', 'https://www.mlb.com'),
            cmsid: _.get(config, 'cmsid', 2493822),
            sz: _.get(config, 'sz', '640x480'),
            ad_rule: _.get(config, 'ad_rule', '1'),
            pp: _.get(config, 'pp', 'mlb_csai_vod_desktop'),
            ciu_szs: _.get(config, 'ciu_szs', '300x100'),
            gdfp_req: _.get(config, 'gdfp_req', '1'),
            env: _.get(config, 'env', 'vp'),
            vid: _.get(config, 'vid', contentId),
            unviewed_position_start: _.get(config, 'unviewed_position_start', '1'),
            playerContext: _.get(config, 'playerContext', 'MLB Home'),
            playerId: _.get(config, 'playerId', 'mlb_video_tray'),
            siteSection: _.get(config, 'siteSection', 'mlb_video_tray'),
            iu: _.get(config, 'iu', '/2605/mlb.video/video_tray/desktop'),
            npa: _.get(config, 'npa', '0'),
            cust_params: encodeCustomParams(custParams)
        };

        // Build the query string
        var query = _.reduce(
            mapper,
            function(result, value, key) {
                return result + (result ? '&' : '') + key + '=' + value;
            },
            ''
        );

        // Construct & return the URL
        var adRequestUrl = url + '?' + query;

        return adRequestUrl;
    }

    /**
     *
     * @desc Builds the zone ad unit structure dynamically based on the provided deviceInfo & arguments
     * IU spec: https://baseball.atlassian.net/wiki/spaces/adopstrafficking/pages/5019907/Web+-+Ad+Manager+Zone+Ad+Unit+Structure
     *
     * @param {object} deviceInfo device specific information via userAgent. From https://github.mlbam.net/fed-packages/device
     * @param {string} networkId (Default "2605")
     * @param {string} adUnit (Default: "mlb.video")
     * @param {string} section (Default: "articles")
     *
     */
    function buildIu(deviceInfo, nId, aU, sect) {
        var formFactor = deviceInfo.formFactor; // desktop, phone, tablet
        var platform = deviceInfo.platform; //ios, andriod
        var device = '';
        var networkId = nId !== undefined ? nId : '2605';
        var adUnit = aU !== undefined ? aU : 'mlb.video';
        var section = sect !== undefined ? sect : 'mlb_video_tray';

        if (platform === 'ios') {
            device = formFactor === 'phone' ? 'iphone' : 'ipad';
        } else if (platform === 'android') {
            device = 'android';
        }

        let iu = '/' + networkId + '/' + adUnit + '/' + section + '/' + formFactor;

        if (device.length > 0) {
            iu = iu + '/' + device;
        }

        return iu;
    }

    return {
    };
});