# Weaviate VectorDB example

Shows how to create a class of questions in Weaviate and how to observe telemetry metrics through Prometheus.

## Necessary Weaviate Docker environment variables

- PROMETHEUS_MONITORING_ENABLED: true
- AUTHENTICATION_ANONYMOUS_ACCESS_ENABLED: true
- PERSISTENCE_DATA_PATH: /var/lib/weaviate
- ENABLE_MODULES: text2vec-openai
- DEFAULT_VECTORIZER: tect2vec-openai
- OPENAI_AIKEY: sk-yourkey

## Docker ports

- 8080: 8080 Weaviate client port
- 2112: 2112 Prometheus port

## Docker compose with local vectorizer

```yaml
version: '3.4'
services:
  weaviate:
    image: name-of-your-weaviate-image
    ports:
      - 8080:8080
    environment:
      CONTEXTIONARY_URL: contextionary:9999
      QUERY_DEFAULTS_LIMIT: 25
      AUTHENTICATION_ANONYMOUS_ACCESS_ENABLED: 'true'
      PERSISTENCE_DATA_PATH: './data'
      ENABLE_MODULES: 'text2vec-contextionary'
      DEFAULT_VECTORIZER_MODULE: 'text2vec-contextionary'
      AUTOSCHEMA_ENABLED: 'false'
  contextionary:
    environment:
      OCCURRENCE_WEIGHT_LINEAR_FACTOR: 0.75
      EXTENSIONS_STORAGE_MODE: weaviate
      EXTENSIONS_STORAGE_ORIGIN: http://weaviate:8080
      NEIGHBOR_OCCURRENCE_IGNORE_PERCENTILE: 5
      ENABLE_COMPOUND_SPLITTING: 'false'
    image: semitechnologies/contextionary:en0.16.0-v1.2.1
```

## Prometheus

URL:2112/metrics

```bash
# HELP batch_durations_ms Duration in ms of a single batch
# TYPE batch_durations_ms histogram
batch_durations_ms_bucket{class_name="Question",operation="object_storage",shard_name="dKT0vwH70XFE",le="10"} 1
batch_durations_ms_bucket{class_name="Question",operation="object_storage",shard_name="dKT0vwH70XFE",le="50"} 1
batch_durations_ms_bucket{class_name="Question",operation="object_storage",shard_name="dKT0vwH70XFE",le="100"} 1
batch_durations_ms_bucket{class_name="Question",operation="object_storage",shard_name="dKT0vwH70XFE",le="500"} 1
batch_durations_ms_bucket{class_name="Question",operation="object_storage",shard_name="dKT0vwH70XFE",le="1000"} 1
batch_durations_ms_bucket{class_name="Question",operation="object_storage",shard_name="dKT0vwH70XFE",le="5000"} 1
batch_durations_ms_bucket{class_name="Question",operation="object_storage",shard_name="dKT0vwH70XFE",le="+Inf"} 1
batch_durations_ms_sum{class_name="Question",operation="object_storage",shard_name="dKT0vwH70XFE"} 3
batch_durations_ms_count{class_name="Question",operation="object_storage",shard_name="dKT0vwH70XFE"} 1
batch_durations_ms_bucket{class_name="Question",operation="vector_storage",shard_name="dKT0vwH70XFE",le="10"} 1
batch_durations_ms_bucket{class_name="Question",operation="vector_storage",shard_name="dKT0vwH70XFE",le="50"} 1
batch_durations_ms_bucket{class_name="Question",operation="vector_storage",shard_name="dKT0vwH70XFE",le="100"} 1
batch_durations_ms_bucket{class_name="Question",operation="vector_storage",shard_name="dKT0vwH70XFE",le="500"} 1
batch_durations_ms_bucket{class_name="Question",operation="vector_storage",shard_name="dKT0vwH70XFE",le="1000"} 1
batch_durations_ms_bucket{class_name="Question",operation="vector_storage",shard_name="dKT0vwH70XFE",le="5000"} 1
batch_durations_ms_bucket{class_name="Question",operation="vector_storage",shard_name="dKT0vwH70XFE",le="+Inf"} 1
batch_durations_ms_sum{class_name="Question",operation="vector_storage",shard_name="dKT0vwH70XFE"} 1
batch_durations_ms_count{class_name="Question",operation="vector_storage",shard_name="dKT0vwH70XFE"} 1
batch_durations_ms_bucket{class_name="n/a",operation="total_api_level",shard_name="n/a",le="10"} 0
batch_durations_ms_bucket{class_name="n/a",operation="total_api_level",shard_name="n/a",le="50"} 0
batch_durations_ms_bucket{class_name="n/a",operation="total_api_level",shard_name="n/a",le="100"} 0
batch_durations_ms_bucket{class_name="n/a",operation="total_api_level",shard_name="n/a",le="500"} 0
batch_durations_ms_bucket{class_name="n/a",operation="total_api_level",shard_name="n/a",le="1000"} 0
batch_durations_ms_bucket{class_name="n/a",operation="total_api_level",shard_name="n/a",le="5000"} 2
batch_durations_ms_bucket{class_name="n/a",operation="total_api_level",shard_name="n/a",le="+Inf"} 2
batch_durations_ms_sum{class_name="n/a",operation="total_api_level",shard_name="n/a"} 4493
batch_durations_ms_count{class_name="n/a",operation="total_api_level",shard_name="n/a"} 2
batch_durations_ms_bucket{class_name="n/a",operation="total_persistence_level",shard_name="n/a",le="10"} 2
batch_durations_ms_bucket{class_name="n/a",operation="total_persistence_level",shard_name="n/a",le="50"} 2
batch_durations_ms_bucket{class_name="n/a",operation="total_persistence_level",shard_name="n/a",le="100"} 2
batch_durations_ms_bucket{class_name="n/a",operation="total_persistence_level",shard_name="n/a",le="500"} 2
batch_durations_ms_bucket{class_name="n/a",operation="total_persistence_level",shard_name="n/a",le="1000"} 2
batch_durations_ms_bucket{class_name="n/a",operation="total_persistence_level",shard_name="n/a",le="5000"} 2
batch_durations_ms_bucket{class_name="n/a",operation="total_persistence_level",shard_name="n/a",le="+Inf"} 2
batch_durations_ms_sum{class_name="n/a",operation="total_persistence_level",shard_name="n/a"} 8.658325
batch_durations_ms_count{class_name="n/a",operation="total_persistence_level",shard_name="n/a"} 2
batch_durations_ms_bucket{class_name="n/a",operation="total_preprocessing",shard_name="n/a",le="10"} 0
batch_durations_ms_bucket{class_name="n/a",operation="total_preprocessing",shard_name="n/a",le="50"} 0
batch_durations_ms_bucket{class_name="n/a",operation="total_preprocessing",shard_name="n/a",le="100"} 0
batch_durations_ms_bucket{class_name="n/a",operation="total_preprocessing",shard_name="n/a",le="500"} 0
batch_durations_ms_bucket{class_name="n/a",operation="total_preprocessing",shard_name="n/a",le="1000"} 0
batch_durations_ms_bucket{class_name="n/a",operation="total_preprocessing",shard_name="n/a",le="5000"} 2
batch_durations_ms_bucket{class_name="n/a",operation="total_preprocessing",shard_name="n/a",le="+Inf"} 2
batch_durations_ms_sum{class_name="n/a",operation="total_preprocessing",shard_name="n/a"} 4465.2318319999995
batch_durations_ms_count{class_name="n/a",operation="total_preprocessing",shard_name="n/a"} 2
batch_durations_ms_bucket{class_name="n/a",operation="total_uc_level",shard_name="n/a",le="10"} 0
batch_durations_ms_bucket{class_name="n/a",operation="total_uc_level",shard_name="n/a",le="50"} 0
batch_durations_ms_bucket{class_name="n/a",operation="total_uc_level",shard_name="n/a",le="100"} 0
batch_durations_ms_bucket{class_name="n/a",operation="total_uc_level",shard_name="n/a",le="500"} 0
batch_durations_ms_bucket{class_name="n/a",operation="total_uc_level",shard_name="n/a",le="1000"} 0
batch_durations_ms_bucket{class_name="n/a",operation="total_uc_level",shard_name="n/a",le="5000"} 2
batch_durations_ms_bucket{class_name="n/a",operation="total_uc_level",shard_name="n/a",le="+Inf"} 2
batch_durations_ms_sum{class_name="n/a",operation="total_uc_level",shard_name="n/a"} 4474.007994
batch_durations_ms_count{class_name="n/a",operation="total_uc_level",shard_name="n/a"} 2
# HELP concurrent_queries_count Number of concurrently running query operations
# TYPE concurrent_queries_count gauge
concurrent_queries_count{class_name="Question",query_type="get_graphql"} 0
concurrent_queries_count{class_name="n/a",query_type="batch"} 0
# HELP go_gc_duration_seconds A summary of the pause duration of garbage collection cycles.
# TYPE go_gc_duration_seconds summary
go_gc_duration_seconds{quantile="0"} 5.2266e-05
go_gc_duration_seconds{quantile="0.25"} 0.000113306
go_gc_duration_seconds{quantile="0.5"} 0.000125444
go_gc_duration_seconds{quantile="0.75"} 0.000154811
go_gc_duration_seconds{quantile="1"} 0.000237556
go_gc_duration_seconds_sum 0.000683383
go_gc_duration_seconds_count 5
# HELP go_goroutines Number of goroutines that currently exist.
# TYPE go_goroutines gauge
go_goroutines 36
# HELP go_info Information about the Go environment.
# TYPE go_info gauge
go_info{version="go1.21.4"} 1
# HELP go_memstats_alloc_bytes Number of bytes allocated and still in use.
# TYPE go_memstats_alloc_bytes gauge
go_memstats_alloc_bytes 5.1968856e+07
# HELP go_memstats_alloc_bytes_total Total number of bytes allocated, even if freed.
# TYPE go_memstats_alloc_bytes_total counter
go_memstats_alloc_bytes_total 1.07408976e+08
# HELP go_memstats_buck_hash_sys_bytes Number of bytes used by the profiling bucket hash table.
# TYPE go_memstats_buck_hash_sys_bytes gauge
go_memstats_buck_hash_sys_bytes 1.4806e+06
# HELP go_memstats_frees_total Total number of frees.
# TYPE go_memstats_frees_total counter
go_memstats_frees_total 504028
# HELP go_memstats_gc_sys_bytes Number of bytes used for garbage collection system metadata.
# TYPE go_memstats_gc_sys_bytes gauge
go_memstats_gc_sys_bytes 6.109968e+06
# HELP go_memstats_heap_alloc_bytes Number of heap bytes allocated and still in use.
# TYPE go_memstats_heap_alloc_bytes gauge
go_memstats_heap_alloc_bytes 5.1968856e+07
# HELP go_memstats_heap_idle_bytes Number of heap bytes waiting to be used.
# TYPE go_memstats_heap_idle_bytes gauge
go_memstats_heap_idle_bytes 3.3210368e+07
# HELP go_memstats_heap_inuse_bytes Number of heap bytes that are in use.
# TYPE go_memstats_heap_inuse_bytes gauge
go_memstats_heap_inuse_bytes 6.2537728e+07
# HELP go_memstats_heap_objects Number of allocated objects.
# TYPE go_memstats_heap_objects gauge
go_memstats_heap_objects 73411
# HELP go_memstats_heap_released_bytes Number of heap bytes released to OS.
# TYPE go_memstats_heap_released_bytes gauge
go_memstats_heap_released_bytes 2.7287552e+07
# HELP go_memstats_heap_sys_bytes Number of heap bytes obtained from system.
# TYPE go_memstats_heap_sys_bytes gauge
go_memstats_heap_sys_bytes 9.5748096e+07
# HELP go_memstats_last_gc_time_seconds Number of seconds since 1970 of last garbage collection.
# TYPE go_memstats_last_gc_time_seconds gauge
go_memstats_last_gc_time_seconds 1.700993853429949e+09
# HELP go_memstats_lookups_total Total number of pointer lookups.
# TYPE go_memstats_lookups_total counter
go_memstats_lookups_total 0
# HELP go_memstats_mallocs_total Total number of mallocs.
# TYPE go_memstats_mallocs_total counter
go_memstats_mallocs_total 577439
# HELP go_memstats_mcache_inuse_bytes Number of bytes in use by mcache structures.
# TYPE go_memstats_mcache_inuse_bytes gauge
go_memstats_mcache_inuse_bytes 2400
# HELP go_memstats_mcache_sys_bytes Number of bytes used for mcache structures obtained from system.
# TYPE go_memstats_mcache_sys_bytes gauge
go_memstats_mcache_sys_bytes 15600
# HELP go_memstats_mspan_inuse_bytes Number of bytes in use by mspan structures.
# TYPE go_memstats_mspan_inuse_bytes gauge
go_memstats_mspan_inuse_bytes 381360
# HELP go_memstats_mspan_sys_bytes Number of bytes used for mspan structures obtained from system.
# TYPE go_memstats_mspan_sys_bytes gauge
go_memstats_mspan_sys_bytes 554064
# HELP go_memstats_next_gc_bytes Number of heap bytes when next garbage collection will take place.
# TYPE go_memstats_next_gc_bytes gauge
go_memstats_next_gc_bytes 1.0271428e+08
# HELP go_memstats_other_sys_bytes Number of bytes used for other system allocations.
# TYPE go_memstats_other_sys_bytes gauge
go_memstats_other_sys_bytes 810288
# HELP go_memstats_stack_inuse_bytes Number of bytes in use by the stack allocator.
# TYPE go_memstats_stack_inuse_bytes gauge
go_memstats_stack_inuse_bytes 720896
# HELP go_memstats_stack_sys_bytes Number of bytes obtained from system for stack allocator.
# TYPE go_memstats_stack_sys_bytes gauge
go_memstats_stack_sys_bytes 720896
# HELP go_memstats_sys_bytes Number of bytes obtained from system.
# TYPE go_memstats_sys_bytes gauge
go_memstats_sys_bytes 1.05439512e+08
# HELP go_threads Number of OS threads created.
# TYPE go_threads gauge
go_threads 9
# HELP lsm_active_segments Number of currently present segments per shard
# TYPE lsm_active_segments gauge
lsm_active_segments{class_name="Question",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/objects",shard_name="dKT0vwH70XFE",strategy="replace"} 1
lsm_active_segments{class_name="Question",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property__id",shard_name="dKT0vwH70XFE",strategy="setcollection"} 1
lsm_active_segments{class_name="Question",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer",shard_name="dKT0vwH70XFE",strategy="roaringset"} 1
lsm_active_segments{class_name="Question",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 1
lsm_active_segments{class_name="Question",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category",shard_name="dKT0vwH70XFE",strategy="roaringset"} 1
lsm_active_segments{class_name="Question",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 1
lsm_active_segments{class_name="Question",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question",shard_name="dKT0vwH70XFE",strategy="roaringset"} 1
lsm_active_segments{class_name="Question",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 1
# HELP lsm_bloom_filters_duration_ms Duration of bloom filter operations
# TYPE lsm_bloom_filters_duration_ms summary
lsm_bloom_filters_duration_ms_sum{class_name="Question",operation="get_false_positive",shard_name="dKT0vwH70XFE",strategy="replace"} 0
lsm_bloom_filters_duration_ms_count{class_name="Question",operation="get_false_positive",shard_name="dKT0vwH70XFE",strategy="replace"} 0
lsm_bloom_filters_duration_ms_sum{class_name="Question",operation="get_true_negative",shard_name="dKT0vwH70XFE",strategy="replace"} 0
lsm_bloom_filters_duration_ms_count{class_name="Question",operation="get_true_negative",shard_name="dKT0vwH70XFE",strategy="replace"} 0
lsm_bloom_filters_duration_ms_sum{class_name="Question",operation="get_true_positive",shard_name="dKT0vwH70XFE",strategy="replace"} 0
lsm_bloom_filters_duration_ms_count{class_name="Question",operation="get_true_positive",shard_name="dKT0vwH70XFE",strategy="replace"} 0
# HELP lsm_memtable_durations_ms Time in ms for a bucket operation to complete
# TYPE lsm_memtable_durations_ms summary
lsm_memtable_durations_ms_sum{class_name="Question",operation="append",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/objects",shard_name="dKT0vwH70XFE",strategy="replace"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="append",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/objects",shard_name="dKT0vwH70XFE",strategy="replace"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="append",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property__id",shard_name="dKT0vwH70XFE",strategy="setcollection"} 0.027706999999999996
lsm_memtable_durations_ms_count{class_name="Question",operation="append",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property__id",shard_name="dKT0vwH70XFE",strategy="setcollection"} 10
lsm_memtable_durations_ms_sum{class_name="Question",operation="append",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="append",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="append",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="append",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="append",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="append",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="append",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="append",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="append",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="append",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="append",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="append",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="appendMapSorted",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/objects",shard_name="dKT0vwH70XFE",strategy="replace"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="appendMapSorted",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/objects",shard_name="dKT0vwH70XFE",strategy="replace"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="appendMapSorted",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property__id",shard_name="dKT0vwH70XFE",strategy="setcollection"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="appendMapSorted",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property__id",shard_name="dKT0vwH70XFE",strategy="setcollection"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="appendMapSorted",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="appendMapSorted",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="appendMapSorted",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0.036301
lsm_memtable_durations_ms_count{class_name="Question",operation="appendMapSorted",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 17
lsm_memtable_durations_ms_sum{class_name="Question",operation="appendMapSorted",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="appendMapSorted",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="appendMapSorted",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0.026489
lsm_memtable_durations_ms_count{class_name="Question",operation="appendMapSorted",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 10
lsm_memtable_durations_ms_sum{class_name="Question",operation="appendMapSorted",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="appendMapSorted",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="appendMapSorted",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0.33405900000000005
lsm_memtable_durations_ms_count{class_name="Question",operation="appendMapSorted",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 133
lsm_memtable_durations_ms_sum{class_name="Question",operation="get",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/objects",shard_name="dKT0vwH70XFE",strategy="replace"} 0.14269700000000002
lsm_memtable_durations_ms_count{class_name="Question",operation="get",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/objects",shard_name="dKT0vwH70XFE",strategy="replace"} 10
lsm_memtable_durations_ms_sum{class_name="Question",operation="get",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property__id",shard_name="dKT0vwH70XFE",strategy="setcollection"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="get",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property__id",shard_name="dKT0vwH70XFE",strategy="setcollection"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="get",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="get",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="get",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="get",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="get",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="get",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="get",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="get",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="get",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="get",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="get",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="get",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="getBySecondary",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/objects",shard_name="dKT0vwH70XFE",strategy="replace"} 0.009981
lsm_memtable_durations_ms_count{class_name="Question",operation="getBySecondary",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/objects",shard_name="dKT0vwH70XFE",strategy="replace"} 4
lsm_memtable_durations_ms_sum{class_name="Question",operation="getBySecondary",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property__id",shard_name="dKT0vwH70XFE",strategy="setcollection"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="getBySecondary",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property__id",shard_name="dKT0vwH70XFE",strategy="setcollection"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="getBySecondary",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="getBySecondary",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="getBySecondary",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="getBySecondary",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="getBySecondary",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="getBySecondary",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="getBySecondary",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="getBySecondary",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="getBySecondary",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="getBySecondary",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="getBySecondary",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="getBySecondary",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="getCollection",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/objects",shard_name="dKT0vwH70XFE",strategy="replace"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="getCollection",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/objects",shard_name="dKT0vwH70XFE",strategy="replace"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="getCollection",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property__id",shard_name="dKT0vwH70XFE",strategy="setcollection"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="getCollection",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property__id",shard_name="dKT0vwH70XFE",strategy="setcollection"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="getCollection",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="getCollection",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="getCollection",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="getCollection",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="getCollection",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="getCollection",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="getCollection",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="getCollection",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="getCollection",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="getCollection",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="getCollection",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="getCollection",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="getMap",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/objects",shard_name="dKT0vwH70XFE",strategy="replace"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="getMap",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/objects",shard_name="dKT0vwH70XFE",strategy="replace"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="getMap",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property__id",shard_name="dKT0vwH70XFE",strategy="setcollection"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="getMap",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property__id",shard_name="dKT0vwH70XFE",strategy="setcollection"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="getMap",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="getMap",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="getMap",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="getMap",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="getMap",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="getMap",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="getMap",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="getMap",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="getMap",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="getMap",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="getMap",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="getMap",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="put",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/objects",shard_name="dKT0vwH70XFE",strategy="replace"} 0.282883
lsm_memtable_durations_ms_count{class_name="Question",operation="put",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/objects",shard_name="dKT0vwH70XFE",strategy="replace"} 10
lsm_memtable_durations_ms_sum{class_name="Question",operation="put",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property__id",shard_name="dKT0vwH70XFE",strategy="setcollection"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="put",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property__id",shard_name="dKT0vwH70XFE",strategy="setcollection"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="put",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="put",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="put",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="put",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="put",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="put",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="put",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="put",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="put",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="put",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="put",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="put",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="setTombstone",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/objects",shard_name="dKT0vwH70XFE",strategy="replace"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="setTombstone",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/objects",shard_name="dKT0vwH70XFE",strategy="replace"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="setTombstone",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property__id",shard_name="dKT0vwH70XFE",strategy="setcollection"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="setTombstone",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property__id",shard_name="dKT0vwH70XFE",strategy="setcollection"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="setTombstone",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="setTombstone",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="setTombstone",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="setTombstone",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="setTombstone",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="setTombstone",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="setTombstone",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="setTombstone",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="setTombstone",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="setTombstone",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_durations_ms_sum{class_name="Question",operation="setTombstone",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_durations_ms_count{class_name="Question",operation="setTombstone",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
# HELP lsm_memtable_size Size of memtable by path
# TYPE lsm_memtable_size gauge
lsm_memtable_size{class_name="Question",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/objects",shard_name="dKT0vwH70XFE",strategy="replace"} 0
lsm_memtable_size{class_name="Question",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property__id",shard_name="dKT0vwH70XFE",strategy="setcollection"} 0
lsm_memtable_size{class_name="Question",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_size{class_name="Question",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_size{class_name="Question",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_size{class_name="Question",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
lsm_memtable_size{class_name="Question",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question",shard_name="dKT0vwH70XFE",strategy="roaringset"} 0
lsm_memtable_size{class_name="Question",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 0
# HELP lsm_segment_count Number of segments by level
# TYPE lsm_segment_count gauge
lsm_segment_count{class_name="Question",level="0",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/objects",shard_name="dKT0vwH70XFE",strategy="replace"} 1
lsm_segment_count{class_name="Question",level="0",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property__id",shard_name="dKT0vwH70XFE",strategy="setcollection"} 1
lsm_segment_count{class_name="Question",level="0",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer",shard_name="dKT0vwH70XFE",strategy="roaringset"} 1
lsm_segment_count{class_name="Question",level="0",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 1
lsm_segment_count{class_name="Question",level="0",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category",shard_name="dKT0vwH70XFE",strategy="roaringset"} 1
lsm_segment_count{class_name="Question",level="0",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 1
lsm_segment_count{class_name="Question",level="0",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question",shard_name="dKT0vwH70XFE",strategy="roaringset"} 1
lsm_segment_count{class_name="Question",level="0",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection"} 1
# HELP lsm_segment_size Size of segment by level and unit
# TYPE lsm_segment_size gauge
lsm_segment_size{class_name="Question",level="0",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/objects",shard_name="dKT0vwH70XFE",strategy="replace",unit="index"} 520
lsm_segment_size{class_name="Question",level="0",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/objects",shard_name="dKT0vwH70XFE",strategy="replace",unit="payload"} 63979
lsm_segment_size{class_name="Question",level="0",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property__id",shard_name="dKT0vwH70XFE",strategy="setcollection",unit="index"} 720
lsm_segment_size{class_name="Question",level="0",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property__id",shard_name="dKT0vwH70XFE",strategy="setcollection",unit="payload"} 666
lsm_segment_size{class_name="Question",level="0",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer",shard_name="dKT0vwH70XFE",strategy="roaringset",unit="index"} 629
lsm_segment_size{class_name="Question",level="0",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer",shard_name="dKT0vwH70XFE",strategy="roaringset",unit="payload"} 3165
lsm_segment_size{class_name="Question",level="0",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection",unit="index"} 629
lsm_segment_size{class_name="Question",level="0",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_answer_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection",unit="payload"} 778
lsm_segment_size{class_name="Question",level="0",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category",shard_name="dKT0vwH70XFE",strategy="roaringset",unit="index"} 86
lsm_segment_size{class_name="Question",level="0",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category",shard_name="dKT0vwH70XFE",strategy="roaringset",unit="payload"} 438
lsm_segment_size{class_name="Question",level="0",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection",unit="index"} 86
lsm_segment_size{class_name="Question",level="0",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_category_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection",unit="payload"} 344
lsm_segment_size{class_name="Question",level="0",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question",shard_name="dKT0vwH70XFE",strategy="roaringset",unit="index"} 4248
lsm_segment_size{class_name="Question",level="0",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question",shard_name="dKT0vwH70XFE",strategy="roaringset",unit="payload"} 21568
lsm_segment_size{class_name="Question",level="0",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection",unit="index"} 4248
lsm_segment_size{class_name="Question",level="0",path="/var/lib/weaviate/question/dKT0vwH70XFE/lsm/property_question_searchable",shard_name="dKT0vwH70XFE",strategy="mapcollection",unit="payload"} 5649
# HELP object_count Number of currently ongoing async operations
# TYPE object_count gauge
object_count{class_name="Question",shard_name="dKT0vwH70XFE"} 10
# HELP objects_durations_ms Duration of an individual object operation. Also as part of batches.
# TYPE objects_durations_ms summary
objects_durations_ms_sum{class_name="Question",operation="put",shard_name="dKT0vwH70XFE",step="inverted_extend"} 1.543001
objects_durations_ms_count{class_name="Question",operation="put",shard_name="dKT0vwH70XFE",step="inverted_extend"} 10
objects_durations_ms_sum{class_name="Question",operation="put",shard_name="dKT0vwH70XFE",step="inverted_total"} 2.0414369999999997
objects_durations_ms_count{class_name="Question",operation="put",shard_name="dKT0vwH70XFE",step="inverted_total"} 10
objects_durations_ms_sum{class_name="Question",operation="put",shard_name="dKT0vwH70XFE",step="retrieve_previous_determine_status"} 0.495166
objects_durations_ms_count{class_name="Question",operation="put",shard_name="dKT0vwH70XFE",step="retrieve_previous_determine_status"} 10
objects_durations_ms_sum{class_name="Question",operation="put",shard_name="dKT0vwH70XFE",step="total"} 6.149867
objects_durations_ms_count{class_name="Question",operation="put",shard_name="dKT0vwH70XFE",step="total"} 10
objects_durations_ms_sum{class_name="Question",operation="put",shard_name="dKT0vwH70XFE",step="upsert_object_store"} 0.299938
objects_durations_ms_count{class_name="Question",operation="put",shard_name="dKT0vwH70XFE",step="upsert_object_store"} 10
# HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
# TYPE process_cpu_seconds_total counter
process_cpu_seconds_total 1.47
# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 1.048576e+06
# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 28
# HELP process_resident_memory_bytes Resident memory size in bytes.
# TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 6.1075456e+07
# HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
# TYPE process_start_time_seconds gauge
process_start_time_seconds 1.70099349083e+09
# HELP process_virtual_memory_bytes Virtual memory size in bytes.
# TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 1.367625728e+09
# HELP process_virtual_memory_max_bytes Maximum amount of virtual memory available in bytes.
# TYPE process_virtual_memory_max_bytes gauge
process_virtual_memory_max_bytes 1.8446744073709552e+19
# HELP promhttp_metric_handler_requests_in_flight Current number of scrapes being served.
# TYPE promhttp_metric_handler_requests_in_flight gauge
promhttp_metric_handler_requests_in_flight 1
# HELP promhttp_metric_handler_requests_total Total number of scrapes by HTTP status code.
# TYPE promhttp_metric_handler_requests_total counter
promhttp_metric_handler_requests_total{code="200"} 2
promhttp_metric_handler_requests_total{code="500"} 0
promhttp_metric_handler_requests_total{code="503"} 0
# HELP queries_durations_ms Duration of queries in milliseconds
# TYPE queries_durations_ms histogram
queries_durations_ms_bucket{class_name="Question",query_type="get_graphql",le="10"} 0
queries_durations_ms_bucket{class_name="Question",query_type="get_graphql",le="50"} 0
queries_durations_ms_bucket{class_name="Question",query_type="get_graphql",le="100"} 0
queries_durations_ms_bucket{class_name="Question",query_type="get_graphql",le="500"} 2
queries_durations_ms_bucket{class_name="Question",query_type="get_graphql",le="1000"} 2
queries_durations_ms_bucket{class_name="Question",query_type="get_graphql",le="5000"} 2
queries_durations_ms_bucket{class_name="Question",query_type="get_graphql",le="+Inf"} 2
queries_durations_ms_sum{class_name="Question",query_type="get_graphql"} 660
queries_durations_ms_count{class_name="Question",query_type="get_graphql"} 2
# HELP queries_filtered_vector_durations_ms Duration of queries in milliseconds
# TYPE queries_filtered_vector_durations_ms summary
queries_filtered_vector_durations_ms_sum{class_name="Question",operation="filter",shard_name="dKT0vwH70XFE"} 0
queries_filtered_vector_durations_ms_count{class_name="Question",operation="filter",shard_name="dKT0vwH70XFE"} 0
queries_filtered_vector_durations_ms_sum{class_name="Question",operation="filter",shard_name="n/a"} 0
queries_filtered_vector_durations_ms_count{class_name="Question",operation="filter",shard_name="n/a"} 0
queries_filtered_vector_durations_ms_sum{class_name="Question",operation="objects",shard_name="dKT0vwH70XFE"} 0
queries_filtered_vector_durations_ms_count{class_name="Question",operation="objects",shard_name="dKT0vwH70XFE"} 0
queries_filtered_vector_durations_ms_sum{class_name="Question",operation="objects",shard_name="n/a"} 0
queries_filtered_vector_durations_ms_count{class_name="Question",operation="objects",shard_name="n/a"} 0
queries_filtered_vector_durations_ms_sum{class_name="Question",operation="sort",shard_name="dKT0vwH70XFE"} 0
queries_filtered_vector_durations_ms_count{class_name="Question",operation="sort",shard_name="dKT0vwH70XFE"} 0
queries_filtered_vector_durations_ms_sum{class_name="Question",operation="sort",shard_name="n/a"} 0
queries_filtered_vector_durations_ms_count{class_name="Question",operation="sort",shard_name="n/a"} 0
queries_filtered_vector_durations_ms_sum{class_name="Question",operation="vector",shard_name="dKT0vwH70XFE"} 0
queries_filtered_vector_durations_ms_count{class_name="Question",operation="vector",shard_name="dKT0vwH70XFE"} 0
queries_filtered_vector_durations_ms_sum{class_name="Question",operation="vector",shard_name="n/a"} 0
queries_filtered_vector_durations_ms_count{class_name="Question",operation="vector",shard_name="n/a"} 0
# HELP query_dimensions_combined_total The vector dimensions used by any read-query that involves vectors, aggregated across all classes and shards. The sum of all labels for query_dimensions_total should always match this labelless metric
# TYPE query_dimensions_combined_total counter
query_dimensions_combined_total 4608
# HELP query_dimensions_total The vector dimensions used by any read-query that involves vectors
# TYPE query_dimensions_total counter
query_dimensions_total{class_name="Question",operation="nearText",query_type="get_graphql"} 4608
# HELP requests_total Number of all requests made
# TYPE requests_total gauge
requests_total{api="graphql",class_name="Question",query_type="Get",status="ok"} 3
requests_total{api="rest",class_name="",query_type="batch",status="ok"} 2
requests_total{api="rest",class_name="",query_type="misc",status="ok"} 3
requests_total{api="rest",class_name="",query_type="misc",status="user_error"} 3
requests_total{api="rest",class_name="",query_type="nodes",status="ok"} 2
requests_total{api="rest",class_name="Question",query_type="schema",status="ok"} 5
requests_total{api="rest",class_name="Question",query_type="schema",status="user_error"} 2
# HELP startup_durations_ms Duration of individual startup operations in ms
# TYPE startup_durations_ms summary
startup_durations_ms_sum{class_name="Question",operation="hnsw_read_all_commitlogs",shard_name="dKT0vwH70XFE"} 0.153825
startup_durations_ms_count{class_name="Question",operation="hnsw_read_all_commitlogs",shard_name="dKT0vwH70XFE"} 1
startup_durations_ms_sum{class_name="Question",operation="lsm_startup_bucket",shard_name="dKT0vwH70XFE"} 9.581807000000001
startup_durations_ms_count{class_name="Question",operation="lsm_startup_bucket",shard_name="dKT0vwH70XFE"} 8
startup_durations_ms_sum{class_name="Question",operation="lsm_startup_bucket_recovery",shard_name="dKT0vwH70XFE"} 0.406963
startup_durations_ms_count{class_name="Question",operation="lsm_startup_bucket_recovery",shard_name="dKT0vwH70XFE"} 8
startup_durations_ms_sum{class_name="Question",operation="shard_total_init",shard_name="dKT0vwH70XFE"} 7.921834
startup_durations_ms_count{class_name="Question",operation="shard_total_init",shard_name="dKT0vwH70XFE"} 1
# HELP startup_progress A ratio (percentage) of startup progress for a particular component in a shard
# TYPE startup_progress gauge
startup_progress{class_name="Question",operation="hnsw_read_commitlogs",shard_name="dKT0vwH70XFE"} 0
# HELP vector_index_durations_ms Duration of typical vector index operations (insert, delete)
# TYPE vector_index_durations_ms summary
vector_index_durations_ms_sum{class_name="Question",operation="create",shard_name="dKT0vwH70XFE",step="find_and_connect_heuristic"} 0.0010590000000000003
vector_index_durations_ms_count{class_name="Question",operation="create",shard_name="dKT0vwH70XFE",step="find_and_connect_heuristic"} 9
vector_index_durations_ms_sum{class_name="Question",operation="create",shard_name="dKT0vwH70XFE",step="find_and_connect_search"} 0.24854300000000001
vector_index_durations_ms_count{class_name="Question",operation="create",shard_name="dKT0vwH70XFE",step="find_and_connect_search"} 9
vector_index_durations_ms_sum{class_name="Question",operation="create",shard_name="dKT0vwH70XFE",step="find_and_connect_total"} 0.290564
vector_index_durations_ms_count{class_name="Question",operation="create",shard_name="dKT0vwH70XFE",step="find_and_connect_total"} 9
vector_index_durations_ms_sum{class_name="Question",operation="create",shard_name="dKT0vwH70XFE",step="find_and_connect_update_connections"} 0.027253
vector_index_durations_ms_count{class_name="Question",operation="create",shard_name="dKT0vwH70XFE",step="find_and_connect_update_connections"} 9
vector_index_durations_ms_sum{class_name="Question",operation="create",shard_name="dKT0vwH70XFE",step="find_entrypoint"} 0.001137
vector_index_durations_ms_count{class_name="Question",operation="create",shard_name="dKT0vwH70XFE",step="find_entrypoint"} 9
vector_index_durations_ms_sum{class_name="Question",operation="create",shard_name="dKT0vwH70XFE",step="prepare_and_insert_node"} 0.017916
vector_index_durations_ms_count{class_name="Question",operation="create",shard_name="dKT0vwH70XFE",step="prepare_and_insert_node"} 9
vector_index_durations_ms_sum{class_name="Question",operation="create",shard_name="dKT0vwH70XFE",step="total"} 0.5150809999999999
vector_index_durations_ms_count{class_name="Question",operation="create",shard_name="dKT0vwH70XFE",step="total"} 10
vector_index_durations_ms_sum{class_name="Question",operation="create",shard_name="dKT0vwH70XFE",step="update_global_entrypoint"} 0.010971
vector_index_durations_ms_count{class_name="Question",operation="create",shard_name="dKT0vwH70XFE",step="update_global_entrypoint"} 10
# HELP vector_index_maintenance_durations_ms Duration of a sync or async vector index maintenance operation
# TYPE vector_index_maintenance_durations_ms summary
vector_index_maintenance_durations_ms_sum{class_name="Question",operation="grow",shard_name="dKT0vwH70XFE"} 0
vector_index_maintenance_durations_ms_count{class_name="Question",operation="grow",shard_name="dKT0vwH70XFE"} 0
# HELP vector_index_operations Total number of mutating operations on the vector index
# TYPE vector_index_operations gauge
vector_index_operations{class_name="Question",operation="create",shard_name="dKT0vwH70XFE"} 10
vector_index_operations{class_name="Question",operation="delete",shard_name="dKT0vwH70XFE"} 0
# HELP vector_index_size The size of the vector index. Typically larger than number of vectors, as it grows proactively.
# TYPE vector_index_size gauge
vector_index_size{class_name="Question",shard_name="dKT0vwH70XFE"} 1000
# HELP vector_index_tombstone_cleaned Total number of deleted objects that have been cleaned up
# TYPE vector_index_tombstone_cleaned counter
vector_index_tombstone_cleaned{class_name="Question",shard_name="dKT0vwH70XFE"} 0
# HELP vector_index_tombstone_cleanup_threads Number of threads in use to clean up tombstones
# TYPE vector_index_tombstone_cleanup_threads gauge
vector_index_tombstone_cleanup_threads{class_name="Question",shard_name="dKT0vwH70XFE"} 0
# HELP vector_index_tombstones Number of active vector index tombstones
# TYPE vector_index_tombstones gauge
vector_index_tombstones{class_name="Question",shard_name="dKT0vwH70XFE"} 0
```