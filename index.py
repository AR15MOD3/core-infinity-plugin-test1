def create(ctx):
    """那边的装载器叫的就是这一个函数（名字固定）。"""

    def ping(word: str = "", **rest):
        """一个工具的 handler：收关键字参数、交回一句回执。"""
        return f"测试插件收到：{word or '（没写词）'}"

    class Mine:
        def start(self):
            note = ctx.get("log")
            if callable(note):
                note("测试插件起来了")

        def stop(self):
            pass

        def tools(self):
            from telyincore.tools import ToolDef, ToolTag
            return [
                ToolDef(name="test_ping", description="测试用：回一句你给的话。",
                        parameters={"type": "object",
                                    "properties": {"word": {"type": "string"}}},
                        tags=(ToolTag.READ,), handler=ping),
            ]

    return Mine()
