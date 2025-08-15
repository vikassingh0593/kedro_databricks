from kedro.framework.hooks import hook_impl

class SparkHooks:
    @hook_impl
    def after_context_created(self, context) -> None:
        import pyspark
        spark = pyspark.sql.SparkSession.builder.getOrCreate()
