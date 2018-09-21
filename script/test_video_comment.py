import allure
import pytest

import utils
from page.bav_page import BavProxy
from page.main_page import MainProxy
from page.video_page import VideoProxy
from page.write_video_comment_page import WriteVideoCommentProxy
from utils import YamlUtil


def build_write_video_comment_data():
    data = YamlUtil.get_data_by_key("video_comment", "test_write_video_comment")
    print(data)
    data_list = []
    for login in data.values():
        data_list.append((login["kw"], login["title"], login["content"], login["toast"]))
    print("data_list=", data_list)
    return data_list


class TestVideoComment:

    @classmethod
    def setup_class(cls):
        print('setup_class')
        cls.main_proxy = MainProxy()
        cls.bav_proxy = BavProxy()
        cls.video_proxy = VideoProxy()
        cls.write_video_comment_proxy = WriteVideoCommentProxy()

    # @classmethod
    # def teardown_class(cls):
    #     print('teardown_class')
    #     DriverUtil.quit_driver()

    def setup(self):
        # 进入‘我的’页面
        self.main_proxy.to_bav_page()
        pass

    @allure.step("写影评功能")
    @pytest.mark.parametrize("kw,title,content,toast", build_write_video_comment_data())
    def test_write_video_comment(self, kw, title, content, toast):
        print("test_write_note kw={} title={} content={} toast={}".format(kw, title, content, toast))

        # 搜索电影并进入电影详情页面
        self.bav_proxy.to_video_page(kw)
        self.video_proxy.to_write_video_comment_page()

        # 写影评
        self.write_video_comment_proxy.write_video_comment(title, content)

        assert utils.is_exist_toast(toast)
