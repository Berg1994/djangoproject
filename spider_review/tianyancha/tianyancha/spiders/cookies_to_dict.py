class GetCookies(object):

    def string_to_dict(self):
        '''
        把从浏览器中抓包的cookie字符串转化成dict
        :return: 返回字典类型的cookies 键值对
        '''
        item_dict = {}
        cookies = 'ssuid=1254123924; aliyungf_tc=AQAAAGu66SyniAUApQnR3oW53ITEY9Tg; csrfToken=OILvkoyAsxZSgolaBLjg6IKf; TYCID=76cd3cf0aab311e8ab7a5901d7dbe577; undefined=76cd3cf0aab311e8ab7a5901d7dbe577; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1535454846; token=8d0f6f03a2ab4abf92a3cd6adcdeb737; _utm=b86d3438a58a45b6ab910f59354c468c; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODIwMDM1MzE5MiIsImlhdCI6MTUzNTQ1NDg2MiwiZXhwIjoxNTUxMDA2ODYyfQ.CK6e2KrHuXhUdps2gGvyHW3Dl75cuMKbUP6wzQfQFwCN6DVgTCgGBjC_dRPjunLxOe9j9rmyG3LZvQO-5jquZw%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218200353192%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODIwMDM1MzE5MiIsImlhdCI6MTUzNTQ1NDg2MiwiZXhwIjoxNTUxMDA2ODYyfQ.CK6e2KrHuXhUdps2gGvyHW3Dl75cuMKbUP6wzQfQFwCN6DVgTCgGBjC_dRPjunLxOe9j9rmyG3LZvQO-5jquZw; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1535454869; bannerFlag=true'
        for cookie in cookies.split(';'):
            key, value = cookie.split('=', 1)
            # print(key, value)
            item_dict[key] = value
        return item_dict


if __name__ == '__main__':
    get_cookie = GetCookies()
    print(get_cookie.string_to_dict())
