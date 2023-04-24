<template>
  <div>
    <!-- 设置代理 -->
    <el-dialog v-model="state.setAPIDialogVisible" title="设置api" align-center draggable destroy-on-close :close-on-click-modal="false" :close-on-press-escape="false" :show-close="false">
      <el-form label-position="right" label-width="130px">
        <el-form-item label="apiserver地址">
          <el-row>
            <el-col :span="33">
              <el-input v-model="state.apiserver" placeholder="请输入" />
            </el-col>
            <el-col :span="1" class="center-col">

            </el-col>
          </el-row>
        </el-form-item>
      </el-form>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="onCancel">取消</el-button>
          <el-button type="primary" @click="onSetAPIConfirm">确认</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<script setup>
import { ElMessage } from 'element-plus'
import { reactive, watch } from 'vue'

const props = defineProps({
  visible: {
    type: Boolean,
    default: false,
    required: false
  }
})
const emits = defineEmits(['close'])

const state = reactive({
  setAPIDialogVisible: false,
  apiserver: '',
})

watch(
  () => props.visible,
  (visible) => {
    if (visible) {
      onAPI() // 设置代理
    }
  }
)

const onAPI = async () => {
  // 设置api
  state.setAPIDialogVisible = true
  state.apiserver = await window.pywebview.api.storage_get('apiserver')
}

const onCancel = () => {
  state.setAPIDialogVisible = false
  emits('close', state.setAPIDialogVisible)
}

const onSetAPIConfirm = () => {
  // console.log(state.proxyPort, state.proxyPorts)
  if (state.apiserver == '' ) {
    ElMessage({ type: 'warning', message: '请设置API服务器信息', grouping: true })
  }  else {
    state.setAPIDialogVisible = false
    window.pywebview.api.storage_set('apiserver', state.apiserver)
    emits('close', state.setAPIDialogVisible)
  }
}

</script>

<style scoped>
.tip {
  color: #909399;
  font-size: 12px;
}
</style>
