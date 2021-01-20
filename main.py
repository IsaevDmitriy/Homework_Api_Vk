import requests

class VkUser:
    def __init__(self, user_id):
        token = ''
        self.url = 'https://api.vk.com/method/'
        self.params = {
            'access_token': token,
            'v': '5.126'
        }
        self.user_id = user_id

    def __str__(self):
        new_url = 'https://vk.com/id' + str(self.user_id)
        return new_url

    def friends_getMutual(self, other):
        if isinstance(other, VkUser):
            followers_url = self.url + 'friends.getMutual'
            followers_params = {
                'source_uid': self.user_id,
                'target_uid': other.user_id
                }
            res = requests.get(followers_url, params={**self.params, **followers_params})

            list_id = res.json()['response']

            return list_id

    def __and__(self, other):
        if isinstance(other, VkUser):
            list_ = self.friends_getMutual(other)
            users = [VkUser(en) for en in list_]

            return print(users)



user1 = VkUser('id')
user2 = VkUser('id')
user1 & user2


