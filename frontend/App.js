/**
 * 汉越语学习工具 - 完整版 App.js
 * 包含：首页、学习卡片、词根学习、个人中心
 */
import React, { useState, useEffect } from 'react';
import { 
  StyleSheet, View, Text, TouchableOpacity, FlatList, 
  TextInput, ScrollView, SafeAreaView, StatusBar, Alert 
} from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import axios from 'axios';

const API_URL = 'http://localhost:8000';

// ==================== API 服务 ====================
const api = {
  getVocabulary: async (level = 0, limit = 50) => {
    try {
      const response = await axios.get(`${API_URL}/api/vocabulary?level=${level}&limit=${limit}`);
      return response.data;
    } catch (error) {
      return getDemoVocabulary();
    }
  },
  
  createUser: async (username, nativeLang = 'zh', targetLang = 'vi') => {
    try {
      const response = await axios.post(`${API_URL}/api/users`, {
        username,
        native_language: nativeLang,
        target_language: targetLang
      });
      return response.data;
    } catch (error) {
      return { id: 'demo_user', username };
    }
  },
  
  updateProgress: async (userId, vocabId, status) => {
    try {
      await axios.post(`${API_URL}/api/progress?user_id=${userId}`, {
        vocabulary_id: vocabId,
        status
      });
    } catch (error) {
      console.log('进度更新演示');
    }
  }
};

// 演示数据
const getDemoVocabulary = () => [
  { id: '1', word_zh: '你好', word_vi: 'Xin chào', meaning_zh: '你好', meaning_vi: 'Xin chào', level: 0 },
  { id: '2', word_zh: '谢谢', word_vi: 'Cảm ơn', meaning_zh: '谢谢', meaning_vi: 'Cảm ơn', level: 0 },
  { id: '3', word_zh: '再见', word_vi: 'Tạm biệt', meaning_zh: '再见', meaning_vi: 'Tạm biệt', level: 0 },
  { id: '4', word_zh: '是', word_vi: 'Có', meaning_zh: '是', meaning_vi: 'Có', level: 0 },
  { id: '5', word_zh: '不是', word_vi: 'Không', meaning_zh: '不是', meaning_vi: 'Không', level: 0 },
  { id: '6', word_zh: '我', word_vi: 'Tôi', meaning_zh: '我', meaning_vi: 'Tôi', level: 0 },
  { id: '7', word_zh: '你', word_vi: 'Bạn', meaning_zh: '你', meaning_vi: 'Bạn', level: 0 },
  { id: '8', word_zh: '他', word_vi: 'Anh ấy', meaning_zh: '他', meaning_vi: 'Anh ấy', level: 0 },
  { id: '9', word_zh: '她', word_vi: 'Cô ấy', meaning_zh: '她', meaning_vi: 'Cô ấy', level: 0 },
  { id: '10', word_zh: '我们', word_vi: 'Chúng tôi', meaning_zh: '我们', meaning_vi: 'Chúng tôi', level: 0 },
  { id: '11', word_zh: '吃', word_vi: 'Ăn', meaning_zh: '吃', meaning_vi: 'Ăn', level: 0 },
  { id: '12', word_zh: '喝', word_vi: 'Uống', meaning_zh: '喝', meaning_vi: 'Uống', level: 0 },
  { id: '13', word_zh: '来', word_vi: 'Đến', meaning_zh: '来', meaning_vi: 'Đến', level: 0 },
  { id: '14', word_zh: '去', word_vi: 'Đi', meaning_zh: '去', meaning_vi: 'Đi', level: 0 },
  { id: '15', word_zh: '看', word_vi: 'Nhìn', meaning_zh: '看', meaning_vi: 'Nhìn', level: 0 },
];

// ==================== 语音播放 ====================
const speak = (text, lang = 'zh-CN') => {
  if (typeof window !== 'undefined' && window.speechSynthesis) {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = lang;
    utterance.rate = 0.9;
    utterance.pitch = 1.0;
    window.speechSynthesis.speak(utterance);
  }
};

// ==================== 首页 ====================
function HomeScreen({ navigation }) {
  const [vocabulary, setVocabulary] = useState([]);
  const [user, setUser] = useState(null);
  const [showSetup, setShowSetup] = useState(true);
  const [userName, setUserName] = useState('');

  useEffect(() => {
    loadVocabulary();
  }, []);

  const loadVocabulary = async () => {
    const data = await api.getVocabulary();
    setVocabulary(data);
  };

  const handleStart = async () => {
    if (!userName.trim()) {
      Alert.alert('提示', '请输入你的名字');
      return;
    }
    const userData = await api.createUser(userName);
    setUser(userData);
    setShowSetup(false);
  };

  const renderItem = ({ item, index }) => (
    <TouchableOpacity 
      style={styles.card}
      onPress={() => navigation.navigate('Learn', { vocab: item })}
    >
      <View style={styles.cardContent}>
        <View style={styles.cardHeader}>
          <Text style={styles.cardNumber}>{index + 1}</Text>
          <Text style={styles.wordZh}>{item.word_zh}</Text>
          <Text style={styles.wordVi}>{item.word_vi}</Text>
        </View>
        <View style={styles.buttonRow}>
          <TouchableOpacity 
            style={styles.speakButton}
            onPress={() => speak(item.word_zh, 'zh-CN')}
          >
            <Text style={styles.speakButtonText}>🔊 中</Text>
          </TouchableOpacity>
          <TouchableOpacity 
            style={styles.speakButton}
            onPress={() => speak(item.word_vi, 'vi-VN')}
          >
            <Text style={styles.speakButtonText}>🔊 越</Text>
          </TouchableOpacity>
        </View>
      </View>
    </TouchableOpacity>
  );

  if (showSetup) {
    return (
      <SafeAreaView style={styles.container}>
        <StatusBar barStyle="dark-content" />
        <View style={styles.setupContainer}>
          <Text style={styles.title}>欢迎来到</Text>
          <Text style={styles.appTitle}>🇻🇳 汉越语学习工具</Text>
          <Text style={styles.subtitle}>3天极速上线版本</Text>
          
          <TextInput
            style={styles.input}
            placeholder="请输入你的名字"
            value={userName}
            onChangeText={setUserName}
            placeholderTextColor="#999"
          />
          
          <TouchableOpacity style={styles.startButton} onPress={handleStart}>
            <Text style={styles.startButtonText}>🚀 开始学习</Text>
          </TouchableOpacity>
        </View>
      </SafeAreaView>
    );
  }

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="dark-content" />
      <View style={styles.header}>
        <Text style={styles.headerTitle}>你好，{user?.username || userName} 👋</Text>
        <Text style={styles.headerSubtitle}>今日学习目标：15 个词汇</Text>
        <View style={styles.statsRow}>
          <View style={styles.statItem}>
            <Text style={styles.statNumber}>{vocabulary.length}</Text>
            <Text style={styles.statLabel}>已学习</Text>
          </View>
          <View style={styles.statItem}>
            <Text style={styles.statNumber}>0</Text>
            <Text style={styles.statLabel}>掌握</Text>
          </View>
          <View style={styles.statItem}>
            <Text style={styles.statNumber}>7</Text>
            <Text style={styles.statLabel}>连续天数</Text>
          </View>
        </View>
      </View>

      <FlatList
        data={vocabulary}
        renderItem={renderItem}
        keyExtractor={item => item.id}
        contentContainerStyle={styles.list}
        showsVerticalScrollIndicator={false}
      />

      <View style={styles.bottomNav}>
        <TouchableOpacity style={[styles.navItem, styles.navItemActive]}>
          <Text style={styles.navText}>🏠 首页</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.navItem} onPress={() => navigation.navigate('Roots')}>
          <Text style={styles.navText}>🔤 词根</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.navItem} onPress={() => navigation.navigate('Profile')}>
          <Text style={styles.navText}>👤 我的</Text>
        </TouchableOpacity>
      </View>
    </SafeAreaView>
  );
}

// ==================== 学习卡片 ====================
function LearnScreen({ route, navigation }) {
  const { vocab } = route.params;
  const [showAnswer, setShowAnswer] = useState(false);
  const [mastered, setMastered] = useState(false);

  const handleSpeakZh = () => speak(vocab.word_zh, 'zh-CN');
  const handleSpeakVi = () => speak(vocab.word_vi, 'vi-VN');

  const handleMastered = () => {
    setMastered(true);
    setTimeout(() => {
      navigation.goBack();
    }, 500);
  };

  return (
    <SafeAreaView style={styles.container}>
      <TouchableOpacity 
        style={styles.backButton}
        onPress={() => navigation.goBack()}
      >
        <Text style={styles.backText}>← 返回</Text>
      </TouchableOpacity>
      
      <View style={styles.learnContainer}>
        <Text style={styles.learnTitle}>词汇学习</Text>
        
        <View style={[styles.learnCard, mastered && styles.learnCardMastered]}>
          <Text style={styles.learnWordZh}>{vocab.word_zh}</Text>
          <TouchableOpacity onPress={handleSpeakZh}>
            <Text style={styles.speakIcon}>🔊 点击朗读</Text>
          </TouchableOpacity>
        </View>

        {!showAnswer ? (
          <TouchableOpacity 
            style={styles.showAnswerButton}
            onPress={() => setShowAnswer(true)}
          >
            <Text style={styles.showAnswerText}>👁️ 显示答案</Text>
          </TouchableOpacity>
        ) : (
          <View style={styles.answerContainer}>
            <View style={styles.learnCard}>
              <Text style={styles.learnWordVi}>{vocab.word_vi}</Text>
              <TouchableOpacity onPress={handleSpeakVi}>
                <Text style={styles.speakIcon}>🔊 点击朗读</Text>
              </TouchableOpacity>
            </View>
            
            <View style={styles.meaningBox}>
              <Text style={styles.meaningLabel}>中文释义</Text>
              <Text style={styles.meaning}>{vocab.meaning_zh}</Text>
              <Text style={styles.meaningLabel}>越文释义</Text>
              <Text style={styles.meaningVi}>{vocab.meaning_vi}</Text>
            </View>
          </View>
        )}

        <View style={styles.actionButtonRow}>
          <TouchableOpacity 
            style={[styles.actionButton, styles.wrongButton]}
            onPress={() => setShowAnswer(false)}
          >
            <Text style={styles.actionButtonText}>↻ 继续学习</Text>
          </TouchableOpacity>
          <TouchableOpacity 
            style={[styles.actionButton, styles.correctButton]}
            onPress={handleMastered}
          >
            <Text style={styles.actionButtonText}>✅ 已掌握</Text>
          </TouchableOpacity>
        </View>
      </View>
    </SafeAreaView>
  );
}

// ==================== 词根学习 ====================
const ROOT_DATA = [
  { id: '1', root: '汉', vi: 'Hán', meaning: '汉字/中国', example: '汉语、汉越语', level: 0 },
  { id: '2', root: '越', vi: 'Việt', meaning: '越南', example: '越语、汉越语', level: 0 },
  { id: '3', root: '学', vi: 'Học', meaning: '学习', example: '学习、学校', level: 0 },
  { id: '4', root: '语', vi: 'Ngữ', meaning: '语言', example: '语言、越语', level: 0 },
  { id: '5', root: '字', vi: 'Tự', meaning: '文字', example: '文字、汉字', level: 0 },
  { id: '6', root: '文', vi: 'Văn', meaning: '文化/文字', example: '文化、中文', level: 0 },
];

function RootsScreen({ navigation }) {
  const renderItem = ({ item }) => (
    <TouchableOpacity style={styles.card}>
      <View style={styles.cardContent}>
        <View style={styles.rootHeader}>
          <Text style={styles.rootChar}>{item.root}</Text>
          <Text style={styles.rootVi}>{item.vi}</Text>
        </View>
        <Text style={styles.rootMeaning}>{item.meaning}</Text>
        <Text style={styles.rootExample}>📝 {item.example}</Text>
      </View>
    </TouchableOpacity>
  );

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="dark-content" />
      <View style={styles.header}>
        <Text style={styles.headerTitle}>🔤 词根学习</Text>
        <Text style={styles.headerSubtitle}>探索汉越语词根奥秘</Text>
      </View>
      <FlatList
        data={ROOT_DATA}
        renderItem={renderItem}
        keyExtractor={item => item.id}
        contentContainerStyle={styles.list}
      />
      <View style={styles.bottomNav}>
        <TouchableOpacity style={styles.navItem} onPress={() => navigation.navigate('Home')}>
          <Text style={styles.navText}>🏠 首页</Text>
        </TouchableOpacity>
        <TouchableOpacity style={[styles.navItem, styles.navItemActive]}>
          <Text style={styles.navText}>🔤 词根</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.navItem} onPress={() => navigation.navigate('Profile')}>
          <Text style={styles.navText}>👤 我的</Text>
        </TouchableOpacity>
      </View>
    </SafeAreaView>
  );
}

// ==================== 个人中心 ====================
function ProfileScreen({ navigation }) {
  const [stats] = useState({
    totalWords: 101,
    masteredWords: 15,
    learningDays: 7,
    currentLevel: 'L0'
  });

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="dark-content" />
      <View style={styles.profileHeader}>
        <View style={styles.avatar}>
          <Text style={styles.avatarText}>👤</Text>
        </View>
        <Text style={styles.profileName}>学习者</Text>
        <View style={styles.levelBadge}>
          <Text style={styles.levelText}>L0 免费用户</Text>
        </View>
      </View>

      <View style={styles.statsContainer}>
        <View style={styles.statBox}>
          <Text style={styles.statBoxNumber}>{stats.totalWords}</Text>
          <Text style={styles.statBoxLabel}>总词汇</Text>
        </View>
        <View style={styles.statBox}>
          <Text style={styles.statBoxNumber}>{stats.masteredWords}</Text>
          <Text style={styles.statBoxLabel}>已掌握</Text>
        </View>
        <View style={styles.statBox}>
          <Text style={styles.statBoxNumber}>{stats.learningDays}</Text>
          <Text style={styles.statBoxLabel}>学习天数</Text>
        </View>
      </View>

      <View style={styles.menuContainer}>
        <TouchableOpacity style={styles.menuItem}>
          <Text style={styles.menuIcon}>📚</Text>
          <Text style={styles.menuText}>学习记录</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.menuItem}>
          <Text style={styles.menuIcon}>⭐</Text>
          <Text style={styles.menuText}>我的收藏</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.menuItem}>
          <Text style={styles.menuIcon}>⚙️</Text>
          <Text style={styles.menuText}>设置</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.menuItem}>
          <Text style={styles.menuIcon}>💎</Text>
          <Text style={styles.menuText}>升级VIP</Text>
        </TouchableOpacity>
      </View>

      <View style={styles.bottomNav}>
        <TouchableOpacity style={styles.navItem} onPress={() => navigation.navigate('Home')}>
          <Text style={styles.navText}>🏠 首页</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.navItem} onPress={() => navigation.navigate('Roots')}>
          <Text style={styles.navText}>🔤 词根</Text>
        </TouchableOpacity>
        <TouchableOpacity style={[styles.navItem, styles.navItemActive]}>
          <Text style={styles.navText}>👤 我的</Text>
        </TouchableOpacity>
      </View>
    </SafeAreaView>
  );
}

const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Home" component={HomeScreen} options={{ headerShown: false }} />
        <Stack.Screen name="Learn" component={LearnScreen} options={{ headerShown: false }} />
        <Stack.Screen name="Roots" component={RootsScreen} options={{ headerShown: false }} />
        <Stack.Screen name="Profile" component={ProfileScreen} options={{ headerShown: false }} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f5f5f5' },
  
  // 首页样式
  setupContainer: { flex: 1, justifyContent: 'center', alignItems: 'center', padding: 20 },
  title: { fontSize: 20, color: '#666' },
  appTitle: { fontSize: 36, fontWeight: 'bold', color: '#333', marginVertical: 10 },
  subtitle: { fontSize: 14, color: '#999', marginBottom: 40 },
  input: { width: '80%', height: 50, borderWidth: 1, borderColor: '#ddd', borderRadius: 10, paddingHorizontal: 15, fontSize: 16, marginBottom: 20, backgroundColor: 'white' },
  startButton: { backgroundColor: '#4CAF50', paddingHorizontal: 40, paddingVertical: 15, borderRadius: 25 },
  startButtonText: { color: 'white', fontSize: 18, fontWeight: 'bold' },
  
  header: { padding: 20, backgroundColor: 'white' },
  headerTitle: { fontSize: 24, fontWeight: 'bold' },
  headerSubtitle: { fontSize: 14, color: '#666', marginTop: 5 },
  statsRow: { flexDirection: 'row', marginTop: 15 },
  statItem: { flex: 1, alignItems: 'center' },
  statNumber: { fontSize: 24, fontWeight: 'bold', color: '#4CAF50' },
  statLabel: { fontSize: 12, color: '#999', marginTop: 3 },
  
  list: { padding: 15 },
  card: { backgroundColor: 'white', borderRadius: 15, marginBottom: 12, shadowColor: '#000', shadowOffset: { width: 0, height: 2 }, shadowOpacity: 0.1, shadowRadius: 4, elevation: 3 },
  cardContent: { padding: 15 },
  cardHeader: { flexDirection: 'row', alignItems: 'center', marginBottom: 10 },
  cardNumber: { width: 24, height: 24, borderRadius: 12, backgroundColor: '#e8f5e9', color: '#4CAF50', textAlign: 'center', lineHeight: 24, fontSize: 12, fontWeight: 'bold', marginRight: 10 },
  wordZh: { fontSize: 24, fontWeight: 'bold', color: '#333', flex: 1 },
  wordVi: { fontSize: 18, color: '#666' },
  buttonRow: { flexDirection: 'row', gap: 10 },
  speakButton: { backgroundColor: '#e8f5e9', paddingHorizontal: 12, paddingVertical: 6, borderRadius: 15 },
  speakButtonText: { fontSize: 12, color: '#4CAF50' },
  
  bottomNav: { flexDirection: 'row', backgroundColor: 'white', paddingVertical: 12, borderTopWidth: 1, borderTopColor: '#eee' },
  navItem: { flex: 1, alignItems: 'center', paddingVertical: 8 },
  navItemActive: { borderBottomWidth: 2, borderBottomColor: '#4CAF50' },
  navText: { fontSize: 12, color: '#666' },
  
  // 学习卡片样式
  backButton: { padding: 15 },
  backText: { fontSize: 16, color: '#4CAF50' },
  learnContainer: { flex: 1, padding: 20 },
  learnTitle: { fontSize: 20, fontWeight: 'bold', textAlign: 'center', marginBottom: 20 },
  learnCard: { backgroundColor: 'white', padding: 30, borderRadius: 20, alignItems: 'center', marginBottom: 20 },
  learnCardMastered: { backgroundColor: '#e8f5e9' },
  learnWordZh: { fontSize: 42, fontWeight: 'bold', color: '#333' },
  learnWordVi: { fontSize: 36, fontWeight: 'bold', color: '#4CAF50' },
  speakIcon: { fontSize: 18, color: '#4CAF50', marginTop: 15 },
  showAnswerButton: { backgroundColor: '#2196F3', padding: 15, borderRadius: 25, alignItems: 'center', marginBottom: 20 },
  showAnswerText: { color: 'white', fontSize: 16, fontWeight: 'bold' },
  answerContainer: { marginBottom: 20 },
  meaningBox: { backgroundColor: '#fff3e0', padding: 15, borderRadius: 10, marginTop: 15 },
  meaningLabel: { fontSize: 12, color: '#999', marginBottom: 3 },
  meaning: { fontSize: 16, color: '#333', marginBottom: 10 },
  meaningVi: { fontSize: 14, color: '#666' },
  actionButtonRow: { flexDirection: 'row', gap: 15, marginTop: 'auto', paddingBottom: 20 },
  actionButton: { flex: 1, padding: 15, borderRadius: 25, alignItems: 'center' },
  wrongButton: { backgroundColor: '#ff5252' },
  correctButton: { backgroundColor: '#4CAF50' },
  actionButtonText: { color: 'white', fontSize: 14, fontWeight: 'bold' },
  
  // 词根样式
  rootHeader: { flexDirection: 'row', alignItems: 'center', marginBottom: 8 },
  rootChar: { fontSize: 32, fontWeight: 'bold', color: '#333', marginRight: 10 },
  rootVi: { fontSize: 20, color: '#4CAF50' },
  rootMeaning: { fontSize: 14, color: '#666', marginBottom: 5 },
  rootExample: { fontSize: 12, color: '#999' },
  
  // 个人中心样式
  profileHeader: { alignItems: 'center', padding: 30, backgroundColor: 'white' },
  avatar: { width: 80, height: 80, borderRadius: 40, backgroundColor: '#e8f5e9', justifyContent: 'center', alignItems: 'center', marginBottom: 15 },
  avatarText: { fontSize: 36 },
  profileName: { fontSize: 24, fontWeight: 'bold', marginBottom: 10 },
  levelBadge: { backgroundColor: '#fff3e0', paddingHorizontal: 15, paddingVertical: 5, borderRadius: 15 },
  levelText: { color: '#ff9800', fontSize: 12 },
  statsContainer: { flexDirection: 'row', padding: 20, backgroundColor: 'white', marginTop: 1 },
  statBox: { flex: 1, alignItems: 'center' },
  statBoxNumber: { fontSize: 28, fontWeight: 'bold', color: '#4CAF50' },
  statBoxLabel: { fontSize: 12, color: '#999', marginTop: 5 },
  menuContainer: { padding: 15 },
  menuItem: { flexDirection: 'row', alignItems: 'center', backgroundColor: 'white', padding: 15, borderRadius: 10, marginBottom: 10 },
  menuIcon: { fontSize: 20, marginRight: 15 },
  menuText: { fontSize: 16, color: '#333' },
});
