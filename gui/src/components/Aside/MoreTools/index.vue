<template>
  <div class="center-c w100">
    <!-- 主题广场 -->
    <div class="flex1">
      <el-tooltip content="主题广场" placement="top" effect="light">
        <el-button key="plain" size="small" link @click="onOpenStore">
          <SvgIcon name="icon-Store" :size="20"></SvgIcon>
        </el-button>
      </el-tooltip>
    </div>

    <!-- 检测更新 -->
    <BtnUpdate class="flex1" />

    <!-- 更多工具栏 -->
    <el-dropdown>
      <span class="el-dropdown-link">
        <el-button key="plain" size="small" link class="flex1">
          <el-icon size="20">
            <ele-Operation />
          </el-icon>
        </el-button>
      </span>
      <template #dropdown>
        <el-dropdown-menu>
          <el-dropdown-item @click="state.visibleAPIDialog = true">
            <el-icon>
              <ele-Guide />
            </el-icon>
            自定义api-server
          </el-dropdown-item>
          <el-dropdown-item divided @click="state.visibleProxyDialog = true">
            <el-icon>
              <ele-Guide />
            </el-icon>
            设置代理
          </el-dropdown-item>
          <el-dropdown-item divided @click="onSet">
            <el-icon>
              <ele-Cpu />
            </el-icon>
            修改sk码
          </el-dropdown-item>
        </el-dropdown-menu>
      </template>
    </el-dropdown>

    <!-- 设置代理 -->
    <ProxyDialog :visible="state.visibleProxyDialog" @close="onCloseProxyDialog" />

     <!-- 设置apiserver -->
    <ApiDialog :visible="state.visibleAPIDialog" @close="onCloseAPIDialog" />

    <!-- 主题广场 -->
    <ThemeStore />

  </div>
</template>

<script setup>
import { ElMessageBox } from 'element-plus'
import ProxyDialog from '@/components/Aside/MoreTools/ProxyDialog.vue'
import ApiDialog from '@/components/Aside/MoreTools/ApiDialog.vue'
import BtnUpdate from '@/components/Aside/MoreTools/BtnUpdate.vue'
import ThemeStore from '@/components/Aside/MoreTools/ThemeStore.vue'
import { reactive } from 'vue'
import { useStoreAside } from '@/stores/aside'

const storeAside = useStoreAside()
const state = reactive({
  visibleProxyDialog: false,
  visibleAPIDialog: false
})

const onSet = async () => {
  const skOpenAI = await window.pywebview.api.storage_get('skOpenAI')
  // console.log('onSet', skOpenAI)
  // 输入 openAI的sk码
  ElMessageBox.prompt('修改openAI的sk码', '提示消息', {
    confirmButtonText: '确认',
    cancelButtonText: '取消',
    showClose: false,
    closeOnClickModal: false,
    closeOnPressEscape: false,
    inputPlaceholder: skOpenAI,
  }).then(({ value }) => {
    if (value == null) {
      value = ''
    }
    window.pywebview.api.storage_set('skOpenAI', value)
  })
}

const onCloseProxyDialog = (visible) => {
  state.visibleProxyDialog = visible
}

const onCloseAPIDialog = (visible) => {
  state.visibleAPIDialog = visible
}

// 主题商店
const onOpenStore = () => {
  // ElMessage({ type: 'success', message: '主题商店功能正在加紧开发中，敬请期待', grouping: true })
  storeAside.setVisibleThemeStore(!storeAside.visibleThemeStore)
}
</script>

<style scoped></style>
